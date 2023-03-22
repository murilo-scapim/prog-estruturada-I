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

for cod, nome, imc in imcs:
    print(cod, nome, imc)

peso_normal2 = [nome for cod, nome, imc in imcs
                if imc >= 18.50 and imc <= 24.99]
print(peso_normal2)

classificacao = [(e[0], e[1],
                  'Baixo peso' if e[2] <= 18.5 else 'Peso normal'
                  if e[2] >= 18.5 and e[2] <= 24.99 else 'Sobrepeso'
                  if e[2] >= 25 and e[2] <= 29.99 else 'Obesidade')
                 for e in imcs]
print(classificacao)


def classifica_imc(imc):
    if imc <= 18.5:
        return 'Baixo peso'
    elif imc >= 18.5 and imc <= 24.99:
        return 'Peso normal'
    elif imc >= 25 and imc <= 29.99:
        return 'Sobrepeso'
    else:
        return 'Obesidade'


classificacao2 = [(cod, nome, classifica_imc(imc))
                  for cod, nome, imc in imcs]
print(classificacao2)
