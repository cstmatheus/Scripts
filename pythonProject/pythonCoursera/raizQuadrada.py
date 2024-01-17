import math
a = float(input('INFORME O \'A\': '))
b = float(input('INFORME O \'B\': '))
c = float(input('INFORME O \'C\': '))

delta = b**2-(4*a*c)
print(delta)

if delta>0:
   x1 = (-b+math.sqrt(delta))/(2*a)
   x2 = (-b-math.sqrt(delta))/(2*a)
   print('EXISTEM DUAS SOLUCOES:\nX1 = \033[1;35m{}\033[m\nX2 = \033[1;35m{}\033[m'.format(x1, x2))
elif delta==0:
   x1 = (-b + math.sqrt(delta)) / (2 * a)
   print('as soluções da equação são repetidas:\nX1 = \033[1;35m{}\033[m\nX2 = \033[1;35m{}\033[m'.format(x1, x1))
elif delta < 0:
   print('\033[1;31mnão admite solução real\033[m')