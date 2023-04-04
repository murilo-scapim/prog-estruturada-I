class Stack:
    #  construtor da classe
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()


stack = Stack()  # instância a classe Stack
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.size())

print(stack.peek())
stack.pop()
print(stack.peek())
