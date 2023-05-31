from Student import Student
from Node import Node

class HashMap:
    def __init__(self):
        self.buckets = [None for i in range(10)]  # compartimentos

    # resulta em endereços de 0 a 9
    def hash_function(self, cod):
        return cod % 10

    # def insert(self, student):
    #     address = self.hash_function(student.cod)
    #     self.buckets[address] = student

    # separate chaining
    # tratando colisões com listas ligadas
    def insert(self, student):
        address = self.hash_function(student.cod)
        new_node = Node(student)
        if self.buckets[address] is None:
            self.buckets[address] = new_node
        else:
            current = self.buckets[address]
            while current.next:
                current = current.next
            current.next = new_node

    # def get(self, cod):
    #     address = self.hash_function(cod)
    #     return self.buckets[address].name

    def get(self, cod):
        address = self.hash_function(cod)
        current = self.buckets[address]

        while current:
            if current.data.cod == cod:
                return current.data.name
            current = current.next
        return None

    # atualizar o nome de um student
    # def update(self, cod, new_name):
    #     address = self.hash_function(cod)
    #     student = self.buckets[address]
    #     student.name = new_name


student1 = Student(14, "João")
student2 = Student(23, "Maria")
student3 = Student(12, "Paulo")

hashmap = HashMap()
hashmap.insert(student1)
hashmap.insert(student2)
hashmap.insert(student3)

print(hashmap.get(12))
# hashmap.update(12, "Paulo atualizado")
