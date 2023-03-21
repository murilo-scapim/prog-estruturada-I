# var1 = [] list
# var2 = () tuple
# var3 = {} dict

Lista1 = [8, 3, 4, 7, 10, 15, 23]

Lista2 = ['par' if e % 2 == 0 else 'impar'
          for e in Lista1]
print(Lista2)


def verifica(numero):
    if numero % 2 == 0:
        return 'par'
    return 'impar'


Lista3 = [verifica(num) for num in Lista1]
print(Lista3)

imcs = [(1, 'Ana', 23.5), (2, 'João', 18.5),
        (3, 'Marcos', 16.8), (4, 'Maria', 27.7),
        (5, 'Bruce', 30.5)]

# print(imcs[0][2]) imc da pessoa

peso_normal = [e for e in imcs
               if e[2] >= 18.5 and e[2] <= 24.99]
print(peso_normal)
