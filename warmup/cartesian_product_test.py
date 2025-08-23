import pytest
from warmup import cartesian_product

@pytest.mark.parametrize("ranges, output", [
    ([[1], [2]], [[1, 2]]),
    ([[1], []], []),
    ([[1], ['a', 'b']], [[1, 'a'], [1, 'b']]),
    ([[1, 2], ['a', 'b'], ['x', 'y']], [[1, 'a', 'x'], [1, 'a', 'y'],[1, 'b', 'x'],[1, 'b', 'y'], [2, 'a', 'x'],[2, 'a', 'y'],[2, 'b', 'x'],[2, 'b', 'y']])
])
def test_calc_cartesian_product(ranges, output):
    assert set(tuple(x) for x in cartesian_product.calc_cartesian_product(ranges)) == set(tuple(x) for x in output)