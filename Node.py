""" A classe Node é usada para representar
cada elemento da lista encadeada, contendo um atributo
para armazenar o dado e um ponteiro para
o próximo nó da lista """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
