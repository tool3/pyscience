from queue import Queue


class Graph:
    def __init__(self):
        self.adjacency = dict()
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
            neighbors = self.adjacency[current]
            for neighbor in neighbors:
                if not neighbor in visited:
                    visited[neighbor] = True
                    self.queue.enqueue(neighbor)
                    result.append(neighbor)
        print(result)
