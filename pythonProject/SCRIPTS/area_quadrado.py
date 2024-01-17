"""
7.	Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

def areaQuadrado(l):
    area = l ** 2

    area = area * 2
    return area


x = int(input('DIGITE O VALOR DA LATERAL DO QUADRADO: '))

print('DOBRO DA AREA DO QUADRADO: ', areaQuadrado(x))
