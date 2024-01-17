"""
2)	Faça um programa que leia 10 números, coloque-os em um vetor e apresente os valores que
forem maior ou igual a média dos números lidos.
"""

lista = []

for i in range(10):
    x = int(input('DIGITE OS NUMEROS: '))
    lista.append(x)

soma = sum(lista)

media = soma / 10
print('=/' * 30)
for i in lista:
    if (i >= media):
        print('ELEMENTO DA LISTA MAIOR QUE A MEDIA: ', i)
print('=/' * 30)

print(media)
