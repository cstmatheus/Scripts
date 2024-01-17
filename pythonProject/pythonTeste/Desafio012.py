valor = float(input('PRECO: '))

r = (valor * 5)/100

novo = valor-r

print('VALOR ANTERIOR: {}\n valor atual: {:.2f}\n valor do reajust: {:.2f}'.format(valor, novo, r))

