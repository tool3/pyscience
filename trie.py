class Node:
    def __init__(self, val):
        self.val = val
        self.letters = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = Node(None)

    def add_word(self, word, node=None):
        if node is None:
            node = self.root
        first_letter = word[:1]
        new_node = Node(first_letter)
        if len(word) == 0:
            node.isWord = True
            return
        elif not first_letter in node.letters:
            node.letters[first_letter] = new_node
            self.add_word(word[1:], node.letters[first_letter])
        else:
            self.add_word(word[1:], node.letters[first_letter])

    def print(self):
        words = []

        def traverse(node, string=""):
            length = len(node.letters)
            if (length):
                if node.val:
                    string += node.val
                for key in node.letters:
                    if node.letters[key].isWord:
                        string += node.letters[key].val
                        return words.append(string)
                    traverse(node.letters[key], string)
            else:
                words.append(string)
        traverse(self.root)
        print(words)

    def is_word(self, word="", node=None):
        if node is None:
            node = self.root
        while len(word) > 0:
            first_letter = word[:1]
            if first_letter not in node.letters:
                return False
            else:
                node = node.letters[first_letter]
                word = word[1:]
        else:
            return True if node.isWord else False
