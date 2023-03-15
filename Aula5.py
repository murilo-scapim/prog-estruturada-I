precos = [500, 1500, 2000, 25]

novos_precos = []
for preco in precos:
    novos_precos.append(preco * 2)

#  list comprehension
novo_preco2 = [preco * 2 for preco in precos]
print(novo_preco2)

frutas = ['maça', 'laranja',
          'kiwi', 'melão']
novo_frutas = [fruta.upper() for fruta
               in frutas]
print(novo_frutas)

novo_frutas2 = [fruta.upper() for fruta
               in frutas if len(fruta) > 4]
print(novo_frutas2)
