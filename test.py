class Stack(object):
    def __init__(self, items):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

