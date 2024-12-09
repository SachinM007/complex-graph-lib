class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2, weight=1):
        self.add_node(node1)
        self.add_node(node2)
        self.adjacency_list[node1].append((node2, weight))

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def __repr__(self):
        return str(self.adjacency_list)
