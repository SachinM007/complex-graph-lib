---

# Complex Graph Library with Multiple Algorithms

A Python library to create, manipulate, and analyze complex graphs, featuring efficient implementations of key graph algorithms, including Dijkstra's algorithm for shortest paths.

---

## Features
- **Graph Creation**: Add nodes and edges to build directed or undirected graphs.
- **Graph Representation**: Store graphs using adjacency lists for efficiency.
- **Graph Algorithms**:
  - Dijkstra's Algorithm: Compute the shortest path from a source node to all other nodes.
  - (Future Extensions: Add more algorithms like BFS, DFS, Kruskal's, Prim's, etc.)

---

## Project Structure
```
graph-library/
│
├── graph_algorithms/
│   ├── __init__.py               # Module initialization
│   ├── graph.py                  # Core Graph class
│   ├── algorithms.py             # Graph algorithms (e.g., Dijkstra's algorithm)
│
├── tests/
│   ├── test_graph.py             # Unit tests for the Graph class
│   ├── test_algorithms.py        # Unit tests for GraphAlgorithms class
│
├── requirements.txt              # Dependencies
├── tox.ini                       # Configuration for Tox
├── README.md                     # Project documentation
├── setup.py                      # Package setup script
```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/graph-library.git
   cd graph-library
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the Library**:
   ```bash
   pip install .
   ```

---

## Usage

### Creating a Graph
```python
from graph_algorithms.graph import Graph

# Create a directed graph
graph = Graph(is_directed=True)
graph.add_node("A")
graph.add_node("B")
graph.add_edge("A", "B", weight=5)

print(graph.adjacency_list)  # Output: {'A': {'B': 5}, 'B': {}}
```

### Running Dijkstra's Algorithm
```python
from graph_algorithms.graph import Graph
from graph_algorithms.algorithms import GraphAlgorithms

# Create a graph
graph = Graph(is_directed=True)
graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 4)
graph.add_edge("B", "C", 2)
graph.add_edge("B", "D", 6)
graph.add_edge("C", "D", 3)

# Run Dijkstra's Algorithm
result = GraphAlgorithms.dijkstra(graph, source="A")
print(result)  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 6}
```

---

## Testing

### Run Unit Tests
Unit tests ensure the correctness of the library.

1. **Run Tests Using Pytest**:
   ```bash
   pytest
   ```

2. **Run Tests Across Multiple Environments with Tox**:
   ```bash
   tox
   ```

### Mutation Testing
Mutation testing ensures your tests are robust.

1. **Install `mutmut`**:
   ```bash
   pip install mutmut
   ```

2. **Run Mutation Tests**:
   ```bash
   mutmut run --paths-to-mutate graph_algorithms/
   ```

3. **Check Results**:
   ```bash
   mutmut results
   ```

---

## Requirements
- Python 3.8 or higher
- Dependencies (see `requirements.txt`)

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature/your-feature`).
3. Commit your changes.
4. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Future Enhancements
- Add more graph algorithms (e.g., Kruskal's, Prim's, BFS, DFS).
- Add visualization tools for graphs.
- Optimize existing algorithms for performance.

---

Feel free to ask if you'd like further modifications or additions!
