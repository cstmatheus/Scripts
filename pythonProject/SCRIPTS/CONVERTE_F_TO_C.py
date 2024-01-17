"""
9.	Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
o	C = 5 * ((F-32) / 9).
"""
def converte(temp):
    c = 5* ((temp-32)/9)

    return c

temp = float(input('TEMPERATURA EM Fahrenheit: '))

print('CELSIUS: {:.1f}'.format(converte(temp)))
