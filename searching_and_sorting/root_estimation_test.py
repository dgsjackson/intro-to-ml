from searching_and_sorting import root_estimation
import pytest

@pytest.mark.parametrize("a, n, precision, expected", [
    (37563, 6, 3, 5.787),
    (776, 2, 5, 27.85678),
    (8766, 3, 4, 20.6190),
    (91, 5, 6, 2.464951),
    (7777, 7, 7, 3.5960879)
])
def test_calc_root_bisection(a, n, precision, expected):
    assert root_estimation.calc_root_bisection(a, n, precision) == expected

@pytest.mark.parametrize("a, n, precision, expected", [
    (37563, 6, 3, 5.787),
    (776, 2, 5, 27.85678),
    (8766, 3, 4, 20.6190),
    (91, 5, 6, 2.464951),
    (7777, 7, 7, 3.5960879)
])
def test_calc_root_newton_raphson(a, n, precision, expected):
    assert root_estimation.calc_root_newton_raphson(a, n, precision) == expected