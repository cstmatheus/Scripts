def delta(b, a, c):
    d = (b ** 2) - (4 * a * c)

    return d


def bas(b, d, a):
    x1 = float((-b + (d ** (1 / 2))) / (2 * a))
    x2 = float((-b - (d ** (1 / 2))) / (2 * a))

    return print('#X1 = {:.2f}#\n#X2 = {:.2f}#'.format(x1, x2))


def raizq(a):
    raiz = a ** (1 / 2)
    return raiz


# n = float(input('RAIZ DE: '))
# r = n ** (1/2)

op = int(input(
    'DIGITE A OPCAO DESEJADA \n[1] PARA DELTA\n[2] PARA BHASKARA\n[3] PARA RAIZ QUADRADA\n[9] PARA SAIR DO SISTEMA \n'))

while (op != 9):

    # b = float(input('\nDIGITE B: '))

    # a = float(input('\nDIGITE A: '))

    if (op == 1):
        print('\n#################SYSTEM_DELTA#################\n')
        b = float(input('DIGITE B: '))

        a = float(input('DIGITE A: '))

        c = float(input('DIGITE C: '))

        de = delta(b, a, c)
        print('VALOR DELTA: {:.2f}'.format(de))

    elif (op == 2):
        print('\n#################SYSTEM_BHASKARA#################\n')
        b = float(input('DIGITE B: '))

        d = float(input('DIGITE DELTA: '))

        a = float(input('DIGITE A: '))
        bas(b, d, a)
    elif (op == 3):
        a = float(input('DIGITE O VALOR DA RAIZ: '))
        resul = raizq(a)
        print('VALOR DA RAIZ: {}'.format(resul))

    print('##############################################################################\n')

    op = int(input(
        'DIGITE A OPCAO DESEJADA \n[1] PARA DELTA\n[2] PARA BHASKARA\n[3] PARA RAIZ QUADRADA\n[9] PARA SAIR DO SISTEMA \n'))
print('##############################################################################\n')
print('SISTEMA FINALIZADO\n')





