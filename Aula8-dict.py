# {chave: valor for elemento in iteravel}

frutas = ['Maça', 'Pera', 'Kiwi', 'Melão', 'Tomate']
dicio = {frutas.index(fruta): fruta
         for fruta in frutas}
print(dicio)

# print(frase.split(' '))

frase = 'algo escrito aqui algo importante'
dicio2 = {palavra: frase.split(' ').count(palavra)
          for palavra in frase.split(' ')}
print(dicio2)
