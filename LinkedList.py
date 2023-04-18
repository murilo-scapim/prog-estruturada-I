from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    #  inserir um nó no final da lista
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node


linked_list = LinkedList()
linked_list.append('Pera')
linked_list.append('Melão')
linked_list.append('Kiwi')
