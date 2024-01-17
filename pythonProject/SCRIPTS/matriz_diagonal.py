matriz = []

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

matriz.append(lista1)
matriz.append(lista2)
matriz.append(lista3)

for i in range(3):
    for j in range(3):
        print('[{:^5}]'.format(matriz[i][j]), end='')
    print('')



"""DIAGONAL PRIMARIA"""

primaria = [matriz[i][i] for i in range(3)]

print('\nDIAGONAL PRIMARIA ',primaria)

"""diagonal secundaria"""
x = [matriz[i][2-i] for i in range(3)]

print('\nMOSTRA DIAGONAL SECUDARIA: ', x)


