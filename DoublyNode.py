from Node import Node


class DoublyNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None