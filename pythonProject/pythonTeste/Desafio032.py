from datetime import date

ano = int(input('ANO PARA ANALISE OU DIGITE 0 PARA VERIFICAR O ANO ATUAL: '))

if ano == 0:
    ano = date.today().year # PEGA O ANO ATUAL

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0: #CONDICAO ANO BISSEXTO
    print('ANO {} E BISSEXTO'.format(ano))

else:
    print('{} NAO E BISSEXTO'.format(ano))