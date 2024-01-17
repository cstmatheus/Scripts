import math

def conDelta(a, b, c):
    delta = b ** 2 - (4 * a * c)
    print(delta)

    if delta > 0:
        x1 = float((-b + math.sqrt(delta)) / (2 * a))
        x2 = float((-b - math.sqrt(delta)) / (2 * a))
        print('EXISTEM DUAS SOLUCOES:\nX1 = {}\nX2 = {}'.format(x1, x2))
    elif delta == 0:
        x1 = float((-b + math.sqrt(delta)) / (2 * a))
        print('as soluções da equação são repetidas:\nX1 = {}\nX2 = {}'.format(x1, x1))
    elif delta < 0:
        print('não admite solução real')


a = float(input('INFORME O \'A\': '))
b = float(input('INFORME O \'B\': '))
c = float(input('INFORME O \'C\': '))


conDelta(a, b, c)



