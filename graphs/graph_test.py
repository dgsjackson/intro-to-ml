import pytest
from graphs import graph

@pytest.fixture
def test_graph():
    edges = [(0 ,2) , (0 ,3) , (0 ,8) ,(2 ,3) ,(3 ,1) , (3 ,2) , (3 ,5) , (3 ,9) ,(4 ,0) , (4 ,6) , (4 ,8) ,(5 ,7) ,(6 ,3)]
    return graph.Graph(edges)

def test_get_child_ids(test_graph):
    assert sorted(test_graph.get_child_ids(3)) == sorted([1, 2, 9, 5])
    assert sorted(test_graph.get_child_ids(4)) == sorted([0, 8, 6])
    assert sorted(test_graph.get_child_ids(7)) == sorted([])

def test_get_parent_ids(test_graph):
    assert sorted(test_graph.get_parent_ids(3)) == sorted([0, 2, 6])
    assert sorted(test_graph.get_parent_ids(4)) == sorted([])
    assert sorted(test_graph.get_parent_ids(7)) == sorted([5])

def test_get_ids_breadth_first(test_graph):
    assert test_graph.get_ids_breadth_first(4) == [4, 0, 6, 8, 2, 3, 1, 5, 9, 7]

def test_calc_distance(test_graph):
    assert test_graph.calc_distance(0, 2) == 1
    assert test_graph.calc_distance(0, 3) == 1
    assert test_graph.calc_distance(0, 5) == 2
    assert test_graph.calc_distance(0, 7) == 3
    assert test_graph.calc_distance(4, 8) == 1

def test_calc_shortest_path(test_graph):
    assert test_graph.calc_shortest_path(0, 2) == [0, 2]
    assert test_graph.calc_shortest_path(0, 9) == [0, 3, 9]
    assert test_graph.calc_shortest_path(0, 1) == [0, 3, 1]
    assert test_graph.calc_shortest_path(4, 7) == [4, 0, 3, 5, 7]