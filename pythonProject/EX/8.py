"""
Faça um programa que receba um número digitado pelo usuário e calcule
 a soma de todos os números de 1 até ao número digitado. Por exemplo,
  se o usuário digitou o número 4, a saída deve ser 10 (1+2+3+4=10).
"""
conta = 0
n = int(input('DIGITE UM NUMERO: '))

for i in range(1, n+1):

    conta = i + conta
    print(conta)
#print(conta)