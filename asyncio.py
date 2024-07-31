import random
import time

from fastapi import FastAPI
from httpx import AsyncClient
import asyncio

app = FastAPI()


@app.post("/parse_url/")
async def parse_url(url: str) -> str:
    """Parse URL"""
    try:
        async with AsyncClient() as client:
            r = await client.get(url)
            r.raise_for_status()

            parse_time = 0.1 * random.randint(5, 10) if random.random() < 0.1 else 0.1
            await asyncio.sleep(parse_time)

            return f"Parsed {url}"
    except Exception as e:
        return f"Error fetching {url}: {e}"


async def run_test(n_requests: int) -> float:
    """Run"""
    url = "https://httpbin.org/"
    
    async with AsyncClient(app=app, base_url=url) as ac:
            ts = time.time()
            tasks = [ac.post("/parse_url/", params={"url": url}) for _ in range(n_requests)]
            responses = await asyncio.gather(*tasks)
            for response in responses:
                print(response.text)
            return time.time() - ts

if __name__ == "__main__":
    t = asyncio.run(run_test(n_requests=100))
    print(f"Time taken: {t} seconds")
