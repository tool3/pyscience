class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.botton = None
        self.size = 0

    def push(self, val):
        node = Node(val)
        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if not self.top:
            return None
        last = self.top
        self.top = self.top.next
        self.size -= 1
        print(last.val)

    def print(self):
        current = self.top
        values = []
        while current:
            values.append(current.val)
            current = current.next
        print(values)
