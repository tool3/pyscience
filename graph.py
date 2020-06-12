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

    def breadth_first(self, vertex):
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
        return result

    def depth_first(self, vertex, result=[], visited={}):
        if not vertex:
            return None
        result.append(vertex)
        visited[vertex] = True
        for neighbor in self.adjacency[vertex]:
            if not neighbor in visited:
                self.depth_first(neighbor, result, visited)
        return result
