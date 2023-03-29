# {chave: valor for elemento in iteravel}

frutas = ['Maça', 'Pera', 'Kiwi', 'Melão', 'Tomate']
dicio = {frutas.index(fruta): fruta
         for fruta in frutas}
print(dicio)

frase = 'algo escrito aqui algo importante'
# print(frase.split(' '))

dicio2 = {palavra: frase.split(' ').count(palavra)
          for palavra in frase.split(' ')}
print(dicio2)
