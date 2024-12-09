import pytest
from graph_algorithms.graph import Graph
from graph_algorithms.algorithms import GraphAlgorithms

def test_dijkstra():
    g = Graph()
    g.add_edge("A", "B", 1)
    g.add_edge("B", "C", 2)
    g.add_edge("A", "C", 4)

    result = GraphAlgorithms.dijkstra(g, "A")
    assert result["A"] == 0
    assert result["B"] == 1
    assert result["C"] == 3
