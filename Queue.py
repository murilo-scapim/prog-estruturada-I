class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)


queue = Queue()

queue.enqueue("Ana")
queue.enqueue("Paulo")
queue.enqueue("Maria")

print(queue.size())

print(queue.dequeue())

print(queue.size())
