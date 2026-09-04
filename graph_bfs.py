from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex_a, vertex_b):
        self.add_vertex(vertex_a)
        self.add_vertex(vertex_b)

        self.adjacency_list[vertex_a].append(vertex_b)
        self.adjacency_list[vertex_b].append(vertex_a)

    def bfs(self, start):
        if start not in self.adjacency_list:
            return []

        visited = set()
        queue = deque()

        queue.append(start)
        visited.add(start)

        traversal_order = []

        while queue:

            current = queue.popleft()
            traversal_order.append(current)

            for neighbor in self.adjacency_list[current]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order


if __name__ == "__main__":

    graph = Graph()

    connections = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "F"),
        ("E", "F")
    ]

    for vertex_a, vertex_b in connections:
        graph.add_edge(vertex_a, vertex_b)

    print("Graph:")
    for vertex, neighbors in graph.adjacency_list.items():
        print(vertex, "->", neighbors)

    print()

    print("BFS starting from A:")
    print(graph.bfs("A"))