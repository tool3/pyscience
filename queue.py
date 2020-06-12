class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, val):
        node = Node(val)
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def dequeue(self):
        if not self.first:
            return None
        if self.first == self.last:
            self.last = None
        last = self.first
        self.first = self.first.next
        self.length -= 1
        return last.val

    def print(self):
        values = []
        current = self.first
        while current:
            values.append(current.val)
            current = current.next
        return values
