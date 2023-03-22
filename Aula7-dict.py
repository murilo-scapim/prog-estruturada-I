# Dicionário é uma estrutura de dados chave/valor
# Armazena um valor a partir de uma chave

dict0 = {}
dict1 = {1: 'Baby Yoda', 2: 'Yoda'}
dict2 = {'nome': 'Baby Yoda', 'idade': 50}
print(dict2['nome'])
print(dict2['idade'])

dict2['nome'] = 'Yoda'
dict2['idade'] = 900

print(dict2['nome'])
print(dict2['idade'])

print(dict2.keys())  # retorna uma lista com as chaves
print(dict2.values())  # retorna uma lista com os valores
print(dict2.items())
print(dict2.get('nome'))  # retorna o valor com base na chave
print(dict2.get('idade'))
dict2.clear()
