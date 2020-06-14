import math


class BinaryHeap:
    def __init__(self):
        self.values = []

    def add(self, val):
        self.values.append(val)
        self.bubble(val)

    def bubble(self, val):
        index = len(self.values) - 1
        while index != 0:
            parent_index = math.floor((index - 1) / 2)
            parent_value = self.values[parent_index]
            if val <= parent_value:
                break
            self.values[parent_index] = val
            self.values[index] = parent_value
            index = parent_index

    def extract_max(self):
        max = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sink()
        return max

    def sink(self):
        index = 0
        length = len(self.values)
        value = self.values[0]
        while True:
            left_child_index = (index * 2) + 1
            right_child_index = (index * 2) + 2
            swap = None
            if left_child_index < length:
                left_child = self.values[left_child_index]
                if left_child > value:
                    swap = left_child_index

            if right_child_index < length:
                right_child = self.values[right_child_index]
                if swap is not None and right_child > left_child:
                    swap = right_child_index

            if swap == None:
                break
            self.values[index] = self.values[swap]
            self.values[swap] = value
            index = swap
