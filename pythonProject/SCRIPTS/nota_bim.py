"""
4.	Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

print('N1 ')
n1 = float(input())

print('N2')
n2 = float(input())

n3 = float(input('N3 \n'))

n4 = float(input('N4 \n'))

media = (n1 + n2 + n3 + n4) / 4
print('=*' * 30)
if (media < 5):
    print('\tALUNO COM A NOTA {} ESTA REPROVADO'.format(media))

elif (media >= 5):
    print('\tALUNO COM A NOTA {} ESTA APROVADO'.format(media))

print('=*' * 30)
