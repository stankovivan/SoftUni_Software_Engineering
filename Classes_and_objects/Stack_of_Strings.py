class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        result = self.data.pop()
        return result

    def top(self):
        result = self.data[-1]
        return result

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f'[{", ".join(reversed(self.data))}]'
