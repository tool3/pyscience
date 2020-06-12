
from queue import Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.queue = Queue()

    def add(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            current = self.root
            while True:
                if val < current.val:
                    if not current.left:
                        current.left = node
                        break
                    current = current.left
                else:
                    if not current.right:
                        current.right = node
                        break
                    current = current.right

    def breadth_first(self):
        visited = {}
        result = []
        self.queue.enqueue(self.root)
        while self.queue.length:
            current = self.queue.dequeue()
            if not current.val in visited:
                visited[current.val] = True
                result.append(current.val)
                if current.left is not None:
                    self.queue.enqueue(current.left)
                if current.right is not None:
                    self.queue.enqueue(current.right)
        return result

    def depth_first(self):
        result = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            result.append(node.val)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return result
