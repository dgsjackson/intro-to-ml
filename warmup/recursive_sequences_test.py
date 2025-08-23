from warmup import recursive_sequences
import pytest

@pytest.mark.parametrize("n,output", [
    (1, [5]),
    (2, [5, 11]),
    (3, [5, 11, 29]),
    (4, [5, 11, 29, 83])
])
def test_basic_array(n, output):
    assert recursive_sequences.basic_array(n) == output

@pytest.mark.parametrize("n, output", [
    (1, 5),
    (2, 11),
    (3, 29),
    (4, 83)
])
def test_basic_recursive(n, output):
    assert recursive_sequences.basic_recursive(n) == output


@pytest.mark.parametrize("n, output", [
    (1, [25]),
    (2, [25, 76]),
    (3, [25, 76, 38]),
    (4, [25, 76, 38, 19]),
    (5, [25, 76, 38, 19, 58])
])
def test_collatz_array(n, output):
    assert recursive_sequences.collatz_array(n) == output

@pytest.mark.parametrize("n, output", [
    (1, 25),
    (2, 76),
    (3, 38),
    (4, 19),
    (5, 58)
])
def test_collatz_recursive(n, output):
    assert recursive_sequences.collatz_recursive(n) == output

@pytest.mark.parametrize("n, output", [
    (1, [0]),
    (2, [0, 1]),
    (3, [0, 1, 1]),
    (4, [0, 1, 1, 2]),
    (5, [0, 1, 1, 2, 3]),
    (6, [0, 1, 1, 2, 3, 5])
])
def test_fibonacci_array(n, output):
    assert recursive_sequences.fibonacci_array(n) == output

@pytest.mark.parametrize("n, output", [
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5)
])
def test_fibonacci_recursive(n, output):
    assert recursive_sequences.fibonacci_recursive(n) == output

