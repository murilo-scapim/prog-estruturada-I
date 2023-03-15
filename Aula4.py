frutas = ['maça', 'laranja', 'kiwi', 'melão']

for indice in range(len(frutas)):
    print(frutas[indice])

for fruta in frutas:
    print(fruta)

for i in range(5):
    #  escopo da variável fruta é local
    fruta = input('Qual a fruta? ')
    frutas.append(fruta)
