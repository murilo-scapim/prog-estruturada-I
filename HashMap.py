class HashMap:
    def __init__(self):
        self.buckets = [None for i in range(10)]

    # resulta em endereços de 0 a 9
    def hash_function(self, cod):
        return cod % 10

    def insert(self, student):
        address = self.hash_function(student.cod)
        self.buckets[address] = student

    def get(self, cod):
        address = self.hash_function(cod)
        return self.buckets[address].name

    # atualizar o nome de um student
    # def update(self, cod, new_name):


student1 = Student(14, "João")
student2 = Student(23, "Maria")
student3 = Student(12, "Teste")

hashmap = HashMap()
hashmap.insert(student1)
hashmap.insert(student2)
hashmap.insert(student3)

# print(hashmap.buckets)

# print(hashmap.get(12))
# hashmap.update(12, "Nome atualizado")
# print(hashmap.get(12))