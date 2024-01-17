"""
16.	Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da
tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

def calculaOrc(m):
    litro = 18
    valor = 80

    partInteira = m // litro

    valorTotal = valor * partInteira

    return print('\nQUANTIDADE DE LATAS {:.0f}\nVALOR TOTAL {} REAIS\n'.format(partInteira, valorTotal))


# m = float(input('INFORME A QUANTIDADE DE [ METRO QUADRADO ]: \n'))

# a = m / 3

print('=/' * 30)
calculaOrc(36)
print('=/' * 30)

# print('\nQUANTIDADE DE LATAS {:.0f}\nVALOR TOTAL {} REAIS'.format(partInteira, (valorTotal))

# print('\nQUANTIDADE NECESSARIA DE TINTA E [ {}L ] '.format(a))

# print('\nVALOR TOTAL {} REAIS'.format(valorTotal))
