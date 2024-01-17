print('/=' * 30)
print('CALCULADORA')
print('/=' * 30)

op = int(input('[1] SOMA\n[2] SUBTRAIR\n[3] MULTIPLICAR\n[0] SAIR\n'))
print('/=' * 30)
while (op != 0):
    valor1 = float(input('NUMERO 1: '))
    valor2 = float(input('NUMERO 2: '))
    if (op == 1):
        resultado = valor1 + valor2
        print('/=' * 30)
        print('O RESULTADO DA SOMA E {:.0f}'.format(resultado))


    elif (op == 2):
        resultado = valor1 - valor2
        print('/=' * 30)
        print('O RESULTADO DA SUBTRACAO E {:.0f}'.format(resultado))

    elif (op == 3):
        resultado = valor1 * valor2
        print('/=' * 30)
        print('O RESULTADO DA MULTIPLICACAO E {:.0f}'.format(resultado))


    else:
        print('INFORME OPCAO VALIDA !')

    print('/=' * 30)
    op = int(input('[1] SOMA\n[2] SUBTRAIR\n[3] MULTIPLICAR\n[0] SAIR\n'))

print('SISTEMA FINALIZADO')
