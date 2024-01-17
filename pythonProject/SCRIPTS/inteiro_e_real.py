"""
11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o	o produto do dobro do primeiro com metade do segundo .
o	a soma do triplo do primeiro com o terceiro.
o	o terceiro elevado ao cubo.
"""
n1 = int(input('N1: int\n'))

n2 = int(input('N2: int\n'))

n3 = float(input('N3: float\n'))


dobro = n1*2

metade = n2/2

produto = dobro * metade


triplo = (n1 * 3) + n3

cubo = n3**3

print('SOLUCAO 1',dobro)

print('SOLUCAO 2',metade)

print('SOLUCAO 3', cubo)