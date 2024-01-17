n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

if n1 > n2 or n2 > n3:

        print('não está em ordem crescente')
else:
    if n2 > n1 and n2 < n3:
        print('crescente')

