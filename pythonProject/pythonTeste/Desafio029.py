v = int(input('Velocidade: '))


if v > 80:
    print('MULTADO')
    taxa = v - 80
    taxa = taxa*7
    print('DEVERA PAGAR {:.2f} REAIS'.format(taxa))
else:
    print('DE BOA')