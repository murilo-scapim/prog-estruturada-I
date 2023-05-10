from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    #  inserir no final
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

        if current_node.next:
            current_node.next = current_node.next.next
        else:
            return 'Elemento não encontrado'

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return 'Elemento encontrado'
            current = current.next
        return 'Elemento não encontrado'
    
    # add em posição específica
    def add_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            # o for percorre até a posição anterior a passada como param
            for i in range(position - 1):
                if current is None:
                    return 'Posição inválida'
                current = current.next

            new_node.next = current.next
            current.next = new_node

linked_list = LinkedList()
linked_list.append('Pera')
linked_list.append('Melão')
linked_list.append('Kiwi')
linked_list.prepend('Melancia')

linked_list.delete('Kiwi')

linked_list.print_list()

print(linked_list.search('Melancia'))

linked_list.add_at_position('Amora', 3)

linked_list.print_list()
