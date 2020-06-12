from queue import Queue


class Graph:
    def __init__(self):
        self.adjacency = {}
        self.queue = Queue()

    def add_vertex(self, val):
        if not val in self.adjacency:
            self.adjacency[val] = []

    def add_edge(self, src, dst):
        self.adjacency[src].append(dst)
        self.adjacency[dst].append(src)

    def print(self, vertex):
        visited = {vertex: True}
        result = [vertex]
        self.queue.enqueue(vertex)
        while self.queue.length:
            current = self.queue.dequeue()
            for neighbor in self.adjacency[current]:
                if not neighbor in visited:
                    visited[neighbor] = True
                    result.append(neighbor)
                    self.queue.enqueue(self.adjacency[neighbor])
        print(result)


g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")
g.add_edge("D", "F")
g.add_edge("E", "F")
g.print("A")
