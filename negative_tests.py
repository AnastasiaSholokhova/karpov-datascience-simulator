import metrics

def test_non_int_clicks():
    try:
        metrics.ctr(1.5, 2)  # Попробуйте вызвать функцию с нецелым количеством кликов
    except TypeError:
        pass
    else:
        raise AssertionError("Non int clicks not handled")

def test_non_int_views():
    try:
        metrics.ctr(1, 2.5)  # Попробуйте вызвать функцию с нецелым количеством просмотров
    except TypeError:
        pass
    else:
        raise AssertionError("Non int views not handled")

def test_non_positive_clicks():
    try:
        metrics.ctr(-1, 2)  # Попробуйте вызвать функцию с отрицательным количеством кликов
    except ValueError:
        pass
    else:
        raise AssertionError("Non positive clicks not handled")

def test_non_positive_views():
    try:
        metrics.ctr(1, -2)  # Попробуйте вызвать функцию с отрицательным количеством просмотров
    except ValueError:
        pass
    else:
        raise AssertionError("Non positive views not handled")

def test_clicks_greater_than_views():
    try:
        metrics.ctr(5, 2)  # Попробуйте вызвать функцию с количеством кликов больше количества просмотров
    except ValueError:
        pass
    else:
        raise AssertionError("Clicks greater than views not handled")

def test_zero_views():
    try:
        metrics.ctr(1, 0)  # Попробуйте вызвать функцию с нулевым количеством просмотров
    except ValueError:
        pass
    else:
        raise AssertionError("Zero views not handled")

# Запуск всех тестов
test_non_int_clicks()
test_non_int_views()
test_non_positive_clicks()
test_non_positive_views()
test_clicks_greater_than_views()
test_zero_views()
