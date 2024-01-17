"""
Exercício 1 - Removendo elementos repetidos
Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros,
verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista
correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

"""

def remove_repetidos(lista):
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)

    return sorted(lista2)

lista = [2, 2, 4, 2, 3, 3, 1]

x = remove_repetidos(lista)

print('LISTA2', x)