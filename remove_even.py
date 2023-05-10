# Criar uma instância (objeto) da classe LinkedList e chamar o método remove_even
from LinkedList import LinkedList

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(3)
linked_list.append(10)
linked_list.append(5)

linked_list.remove_even()

linked_list.print_list()
