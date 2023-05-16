from DoublyNode import DoublyNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # adiciona um elmento no final
    def append(self, data):
        new_node = DoublyNode(data)

        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node
            new_node.prev = current