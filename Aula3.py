fruta = 'maça'
print(type(fruta))  # tipo de dados da variável

frutas = ['maça', 'laranja', 'kiwi', 'melão']
print(type(frutas))

print(frutas[0])  # primeiro elemento
print(frutas[1])
# print(frutas[4]) # fora do intervalo de índices

print(len(frutas))  # tamanho do vetor, length

print(frutas[-1])

# frutas[0] = 'uva'
print(frutas)

print(frutas[1:3])  # o elem do índice 3 não é incluido

print(frutas[:3])  # não inclue o elem do índice 3
print(frutas[2:])  # começa no elem de índice 2 até o último

frutas.append('laranja')  # inserção no final

frutas.insert(0, 'uva')

frutas.remove('maça')  # remoção de um elem específico

frutas.pop()  # remoção no final
frutas.pop(0)  # remoção passando um índice

frutas.clear()  # esvazia a lista
