"""
Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.

1 x 1
1 x 2


"""

num = int(input('DIGITE O NUMERO: '))

x = range(1, 11)
for n in x:
    # for n in range(5):
    # if n > 0:
    mult = num * n
    print('{} X {} = {}'.format(num, n, mult))
