"""
Escreva a função soma_elementos que recebe como parâmetro uma lista com números
inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.

"""

def soma_elementos(lista):

    cont = lista[0]
    for i in range(1, len(lista)):
        cont = cont + lista[i]
    return cont



lista = sorted([2, 4, 2, 2, 3, 3, 1])

x = soma_elementos(lista)

print(x)

