class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self):
        if not self.head:
            return None
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        last = current
        prev.next = None
        self.tail.next = None
        self.tail = prev
        return last

    def remove(self, val):
        if not self.head:
            return None
        current = self.head
        prev = None
        while current.val != val:
            prev = current
            current = current.next
        if not prev:
            return None
        removed = current
        prev.next = current.next if current.next else None
        self.length -= 1
        return removed

    def print(self):
        values = []
        current = self.head
        while (current):
            values.append(current.val)
            current = current.next
        print(values)

    def reverse(self):
        current = self.head
        prev = None
        while(current):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
