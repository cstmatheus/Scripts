"""
 Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do novo salário reajustado
 de acordo com a tabela abaixo:Salário atual 	Reajuste

                            Abaixo de R$500,00 	15%
                            de R$500,00 até R$1000,00 	10%
                            Acima de R$1000,00 	5%

"""
# num=float(1000)
m = str('\tDIGITE SEU SALARIO: ')

print('{}'.format(m))

sal = float(input())

if (sal < 500):
    reajuste = (sal * 15) / 100
    salatual = sal + reajuste
    # print('O VALOR DO REAJUSTE: {}\nSALARIO ATUAL: {}'.format(reajuste, salatual))

elif (sal >= 500 or sal <= 1000):
    reajuste = (sal * 10) / 100
    salatual = sal + reajuste
    # print('O VALOR DO REAJUSTE: {}\nSALARIO ATUAL: {}'.format(reajuste, salatual))

if(sal > 1001):

    reajuste = (sal * 5) / 100
    salatual = sal + reajuste
    print('O VALOR DO REAJUSTE: {}\nSALARIO ATUAL: {}'.format(reajuste, salatual))


print('OI')
