"""
6.	Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""

def areaCirculo(r):
    a = 3.14*(r**2)

    return a



print('=/'*30)
print('DIGITE O RAIO DO CIRCULO: ')
print('=/'*30)
r = float(input())

print(areaCirculo(r))

#print('AREA {:.2f}'.format(a))
