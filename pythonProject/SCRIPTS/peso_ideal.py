"""
13.	Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
o	Para homens: (72.7*h) - 58
o	Para mulheres: (62.1*h) - 44.7

"""


def althomem(altura):
    pesoideal = (72.2 * altura) - 58

    return pesoideal


def altmulher(altura):
    pesoideal = (62.1 * altura) - 44.7

    return pesoideal


print(althomem(1.65))

print(altmulher(1.65))
