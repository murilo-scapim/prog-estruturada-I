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
    
    # adiciona um elemento no início da lista
    def prepend(self, data):
        new_node = DoublyNode(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def show(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


doubly_node = DoublyLinkedList()
doubly_node.append(1)
doubly_node.append(2)
doubly_node.append(3)
doubly_node.prepend(0)

doubly_node.show()

print(doubly_node.is_empty())
