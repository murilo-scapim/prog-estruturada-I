# Ex 1

Lista1 = [2, 3, 6, 7, 5, 16]
Lista2 = [e*2 for e in Lista1 if e % 2 == 0]
print(Lista2)

# Ex 2
frase = "Sistemas de informação"

nova_lista = [letra for letra in frase if letra != " "]
print(nova_lista)

# Ex 3

lista = ['Ana', 'Alfredo', 'Ely', 'Thomas', 'Jim', 'Joana']

nova_lista = [nome.upper().replace("A", "@") for nome in lista]
print(f"A resposta do exercício 3 é: {nova_lista}")

# Ex 4

def ContVog(nome):
    cont=0
    for letra in nome:
        if letra in "aeiou":
            cont+=1
    return cont

ListaVog=[nome for nome in lista if ContVog(nome.lower()) >= 3]
print(f"A resposta do exercicio 4 é: {ListaVog}")

# Ex 5

frase = "Sistemas de Informação"
VogaisFrase = [letra for letra in frase if letra.lower() in "aeiou"]
print(f"A resposta do exercicio 5 é: {VogaisFrase}")
