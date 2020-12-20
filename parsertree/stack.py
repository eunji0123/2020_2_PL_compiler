class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def peek(self):
        return self.items[-1]
    def pop(self):
        self.items.pop()
    def isEmpty(self):
        return not self.items