km = float(input('QUANTOS KMs ?: '))

qtd = int(input('Qunatos dias?: '))

cd = qtd * 60

kmr = km * 0.15

print('DEVE PAGAR: {:.2f}'.format(cd+kmr))
