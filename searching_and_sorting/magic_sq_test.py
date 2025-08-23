import pytest
from searching_and_sorting import magic_sq_backtracking

@pytest.mark.parametrize("input, output", [
    ([[0,0,0],[0,0,0],[0,0,0]], False),
    ([[1,2,3],[0,0,0],[0,0,0]], True),
    ([[1,0,0],[2,0,0],[3,0,0]], True),
    ([[1,0,0],[0,2,0],[0,0,3]], True),
    ([[0,0,1],[0,2,0],[3,0,0]], True),
    ([[7,8,0],[0,0,0],[0,0,0]], True),
    ([[7,1,8],[0,0,0],[0,0,0]], True),
    ([[7,0,0],[0,8,0],[0,0,0]], True),
    ([[0,0,7],[0,0,8],[0,0,0]], True),
    ([[0,0,7],[0,0,6],[0,0,0]], False),
    ([[7,5,0],[0,0,0],[0,0,0]], False),
    ([[3,0,0],[5,4,0],[0,0,1]], True),
])
def test_is_hopeless(input, output):
    assert magic_sq_backtracking.is_hopeless(input) == output