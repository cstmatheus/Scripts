"""
Escreva a função maior_elemento que recebe como parâmetro uma lista com números
 inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.
"""

def maior_elemento(lista):
    maior = lista[0]
    for i in range(len(lista)):

        lista.append(i)

        if lista[i] > maior:
            maior = lista[i]
    return maior

lista = [-90, -27, -12]

s = maior_elemento(lista)

print(s)









