from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    # insere no final
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    # insere no inicio
    def prepend(self, data):
        new_node = Node(data)

        # if not self.head:
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    # remove um elemento especifico
    def delete(self, data):
        if self.head is None:
            return 'Lista vazia'

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

            if curent_node.next:
                current_node.next = current_node.next.next
            else:
                return 'Elemento não econtrado'
            
    # Implementar para próxima aula
    # def print_list(self):


linked_list = LinkedList()
linked_list.append('Pera')
linked_list.append('Melão')
linked_list.append('Kiwi')
linked_list.prepend('Melancia')

linked_list.delete('Kiwi')
