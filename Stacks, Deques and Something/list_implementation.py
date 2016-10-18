class List(object):
    def __init__(self):
        self.items = []

    def enqueue(self, items):
        self.items.append(items)
