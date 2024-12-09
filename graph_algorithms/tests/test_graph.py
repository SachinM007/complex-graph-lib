import pytest
from graph_algorithms.graph import Graph

def test_add_node():
    g = Graph()
    g.add_node("A")
    assert "A" in g.adjacency_list

def test_add_edge():
    g = Graph()
    g.add_edge("A", "B", 5)
    assert g.get_neighbors("A") == [("B", 5)]
