import math
a = float(input('INFORME O \'A\': '))
b = float(input('INFORME O \'B\': '))
c = float(input('INFORME O \'C\': '))

delta = b**2-(4*a*c)

if delta>0:
   x1 = (-b+math.sqrt(delta))/(2*a)
   x2 = (-b-math.sqrt(delta))/(2*a)
   if x1<x2:
      print('1as raízes da equação são {} e {}'.format(x1, x2))
   else:
      if x2<x1:
         print('as raízes da equação são {} e {}'.format(x2, x1))

elif delta==0:
   x1 = (-b+math.sqrt(delta)) / (2*a)
   print('a raiz desta equação é {}'.format(x1))

elif delta < 0:
   print('esta equação não possui raízes reais')