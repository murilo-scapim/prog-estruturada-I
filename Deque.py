from collections import deque


class Deque:
    def __init__(self):
        self.items = deque()
        
    # Docstring
    def is_empty(self):
        """
        Verifica se o Deque está vazio.
        :return: True se o deque estiver vazio, caso contrário False
        """
        return not bool(self.items)

    def add_front(self, item):
        self.items.appendleft(item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            return None
        return self.items.popleft()

    def remove_rear(self):
        if self.is_empty():
            return None
        return self.items.pop()

      
d = Deque()

d.add_front('Ana')
d.add_front('Maria')
d.add_rear('Paulo')
d.add_rear('João')

d.is_empty()

d.remove_front()

d.remove_rear()
