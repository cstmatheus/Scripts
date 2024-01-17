num = int(input('Digite um número inteiro: '))

uni = num
cont = num
a = 1
x = 0

while cont > -1:
    #UNI DESCSCA CADA DIGITO
    uni = (num // a % 10)
    #'a' ESTA MULTIPLICANDO POR 10 A CADA INTECAO PARA QUE AS CASA SEJAM SEGUIDAS
    a *= 10
    #'x' ESTA SOMANDO CADA CASA
    x = x + uni
    #cont ESTA CONTROLANDO A INTERACAO, COM O VALOR DE 'NUM' COM A SUBTRACAO DE 'a' QUE E MULTIPLICADO POR 10 PARA
    #SEGUIR PARA A OUTRA CASA
    cont = num - a

print(x)