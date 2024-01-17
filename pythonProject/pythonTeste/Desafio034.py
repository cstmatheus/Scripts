sal = float(input('SALARIO: '))

if(sal> 1250):

    ac = (sal*10)/100

    print('reajuste de 10% {}'.format(ac))
    print('VALOR TORAL {}'.format(sal + ac))

elif (sal <= 1250):

    ac = (sal*15)/100

    print('reajuste de 15% {}'.format(ac))
    print('VALOR TORAL {}'.format(sal + ac))
