from typing import Dict, Tuple

import numpy as np
from sklearn.datasets import make_regression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def prepare_data():
    X, y = make_regression(n_samples=1000, n_features=10, noise=0.2, random_state=42)
    return X, y


def solution(data: Tuple[np.ndarray, np.ndarray]) -> Dict[str, np.ndarray]:
    lr = LinearRegression()
    X, y = data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return {
        "y_pred": y_pred,
        "y_test": y_test,
        "mse": mse,
        "mae": mae,
        "r2": r2,
    }


if __name__ == "__main__":
    data = prepare_data()
    metrics = solution(data)
    print("MSE:", metrics["mse"])
    print("MAE:", metrics["mae"])
    print("R2:", metrics["r2"])
