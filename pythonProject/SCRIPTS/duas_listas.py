"""
1	- Crie 2 listas: uma com 5 nomes(João, Maria, Kleber, Caio e Sarah) e outra com 5 valores em reais(R$)
correspondentes ao saldo da conta do usuário(1350,20; 240,50; 30,00; 830,15 e 50,00), e usando laços de repetição
 imprima os dados da seguinte forma(o preenchimento das listas deve ser feito também com laços de repetição do mesmo
  modo que será impresso: salvar nome e depois salvar o saldo correspondente):
Entradas:
Insira o nome: **** Insira o saldo: ****

"""

msg1 = 'DIGITE O NOME: '

msg1 = msg1.lower()

msg2 = 'digite o saldo: '

msg2 = msg2.upper()

lista1 = []
lista2 = []
lista3 = []

print('==' * 30)
for i in range(1, 3):
    print('ID: ', i)
    nome = input(msg1)
    saldo = input(msg2)

    lista1.append(nome)
    lista2.append(saldo)
    lista3.append(i)
    print('==' * 30)

msg3 = 'REGISTROS CADASTRADOS'

print('[{:^58}]'.format(msg3))
print('==' * 30)

for i in range(0, 2):
    # print('INDICE ', i)
    print('ID: ', lista3[i])
    print('NOME: ', lista1[i])
    print('SALDO: ', lista2[i])
    print('==' * 30)
