valor = float(input('Valor ?\n'))

taxa = int(input('Taxa ?\n'))

print('VALOR INFORMADO \033[1;34m{}\033[m, TAXA INFORMADA \033[1;34m{}\033[m\nVALOR ATUALIZADO \033[1;32m{:.2f}\033[m'
      .format(valor, taxa, valor+(valor*taxa)/100).replace('.', ','))
