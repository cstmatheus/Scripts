"""
15.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
  8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
o	salário bruto.
o	quanto pagou ao INSS.
o	quanto pagou ao sindicato.
o	o salário líquido.
o	calcule os descontos e o salário líquido, conforme a tabela abaixo:
o	+ Salário Bruto : R$
o	- IR (11%) : R$
o	- INSS (8%) : R$
o	- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

salario = float(input('QUANTO GANHA POR HORA: '))

hora = float(input('HORAS TRABALHADAS: '))

t = salario * hora

inrenda = (11*t)/100

inss =  (8*t)/100

sind = (5*t)/100

desconto = inrenda + inss + sind

liquido = t - desconto

print('/='*30)

print('+ Salário Bruto : R${}\n	- IR (11%) : R${}\n	- INSS (8%) : R${}\n	- Sindicato ( 5%) : R${}\n    - Salário Liquido : R${}\n    - TOTAL DESCONTO : R${}'.format(t, inrenda, inss, sind, liquido, desconto ))

print('/='*30)

