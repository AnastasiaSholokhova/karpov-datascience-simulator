from typing import List
from functools import reduce

def sales_with_tax(sales: List[float], tax_rate: float, threshold: float = 300) -> List[float]:
    """Задание 1"""
    big_nums = filter(lambda x: x > threshold, sales)
    taxes = list(map(lambda x: x  * (1 + tax_rate), big_nums))
    return taxes

def sum_sales(sales: List[float], threshold: float = 300) -> float:
    """Задание 2"""
    min_sales = list(filter(lambda x: x >= threshold, sales))
    sum_sales = reduce(lambda x, y: x + y, min_sales, 0.0)
    return sum_sales

def average_age(ages: List[int], threshold: int = 30) -> float:
    """Задание 3"""
    big_years = list(filter(lambda x: x > threshold, ages))
    total = reduce(lambda x, y: x + y, big_years)
    length = len(big_years)
    avg_year = total/length if length > 0 else 0
    return avg_year

def increased_prices(prices: List[float], increase_rate: float = 0.2, threshold: float = 300) -> List[float]:
    """Задание 4"""
    summed_prices = map(lambda x: x * (1 + increase_rate), prices)
    filtered_prices = list(filter(lambda x: x > threshold, summed_prices))
    return filtered_prices

def weighted_sale_price(sales: List[tuple]) -> float:
    """Задание 5"""
    total_price = reduce(lambda acc, sale: acc + sale, map(lambda x: x[0] * x[1], sales), 0)
    total_quantity = reduce(lambda acc, sale: acc + sale, map(lambda x: x[1], sales), 0)
    weighted_average = total_price / total_quantity if total_quantity > 0 else 0
    return weighted_average