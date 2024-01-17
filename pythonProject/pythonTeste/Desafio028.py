import random

n = int(input('Numero: '))

r = random.randint(0, 5)

if n == r:
    print('ACERTOU NUMERO PENSADO FOI {}'.format(r))
else:
    print('ERROU O NUMERO PENSADO FOI {}'.format(r))

