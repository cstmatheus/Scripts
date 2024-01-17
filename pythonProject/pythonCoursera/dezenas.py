"""
1 OPCAO
num = 1894

unidade = num // 1 % 10 # 4
dezena = num // 10 % 10 # 9
centena = num // 100 % 10 # 8
milhar = num // 1000 % 10 # 1
===================================================================================
2 OPCAO - Transforma para String, depois aponta o local do número.

num = int(input('Entre com um número de 0 a 9999: '))
n = str(num)

print('\nAnalizando o número {}'.format(n))
print('\nUnidade: {}'
    '\nDezena: {}'
    '\nCentena: {}'
    '\nMilhar: {}'
    .format(n[3], n[2], n[1], n[0])
      )
"""

n = int(input('Digite um número inteiro: '))

dezena = n // 10 % 10

print('O dígito das dezenas é {}'.format(dezena))