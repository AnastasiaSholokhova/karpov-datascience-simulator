import numpy as np


def mean_squared_error(actual: np.ndarray, predicted: np.ndarray) -> float:
    """Mean squared error calculation"""
    mse = np.square(np.subtract(actual, predicted)).mean()
    return mse


def root_mean_squared_error(actual: np.ndarray, predicted: np.ndarray) -> float:
    """Root mean squared error calculation"""
    rmse = np.sqrt(np.square(np.subtract(actual, predicted)).mean())
    return rmse

def mean_absolute_error(actual: np.ndarray, predicted: np.ndarray) -> float:
    """Mean absolute error calculation"""
    mae = np.abs(np.subtract(actual, predicted)).mean()
    return mae


def mean_absolute_percentage_error(actual: np.ndarray, predicted: np.ndarray) -> float:
    """Mean absolute percentage error calculation"""
    mape = np.mean(np.abs((actual - predicted) / actual))*100
    return mape


def r_squared(actual: np.ndarray, predicted: np.ndarray) -> float:
    """R2 calculation"""
    mean_actual = np.mean(actual)
    ss_res = np.sum(np.square(actual - predicted))
    ss_tot = np.sum(np.square(actual - mean_actual))
    r2 = 1 - (ss_res / ss_tot)
    return r2


def test():
    """Tests"""
    actual = np.array([3, -0.5, 2, 7])
    predicted = np.array([2.5, 0.0, 2, 8])

    assert np.allclose(mean_squared_error(actual, predicted), 0.375)
    assert np.allclose(root_mean_squared_error(actual, predicted), 0.6123724356957945)
    assert np.allclose(mean_absolute_error(actual, predicted), 0.5)
    assert np.allclose(
        mean_absolute_percentage_error(actual, predicted), 32.73809523809524
    )
    assert np.allclose(r_squared(actual, predicted), 0.9486081370449679)

    print("All tests passed.")


if __name__ == "__main__":
    test()