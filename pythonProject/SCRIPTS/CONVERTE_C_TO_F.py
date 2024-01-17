"""
9.	Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
o	C = 5 * ((F-32) / 9).
"""
m = 'CONVERSAO celsius para Fahrenheit'


print('{}'.format(m))

cel= float(input())

con = (cel * 1.8) + 32


print('VALOR CONVERTIDO {:.0f}'.format(con))
