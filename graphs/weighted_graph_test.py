import pytest
from graphs import weighted_graph

@pytest.fixture
def test_graph():
    weights = {
(0 ,1) : 3, (1 ,0) : 3,
(1 ,7) : 4, (7 ,1) : 4,
(7 ,2) : 2, (2 ,7) : 2,
(2 ,5) : 1, (5 ,2) : 1,
(5 ,6) : 8, (6 ,5) : 8,
(0 ,3) : 2, (3 ,0) : 2,
(3 ,2) : 6, (2 ,3) : 6,
(3 ,4) : 1, (4 ,3) : 1,
(4 ,8) : 8, (8 ,4) : 8,
(8 ,0) : 4, (0 ,8) : 4
}
    graph = weighted_graph.WeightedGraph(weights)
    return graph

def test_calc_distance(test_graph):
    assert test_graph.calc_distance(8, 0) == 4
    assert test_graph.calc_distance(8, 1) == 7
    assert test_graph.calc_distance(8, 2) == 12
    assert test_graph.calc_distance(8, 3) == 6
    assert test_graph.calc_distance(8, 4) == 7
    assert test_graph.calc_distance(8, 5) == 13
    assert test_graph.calc_distance(8, 6) == 21
    assert test_graph.calc_distance(8, 7) == 11
    assert test_graph.calc_distance(8, 8) == 0
