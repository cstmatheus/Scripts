soma = 0
a = 1
c = 0
z = 0
x = int(input('INFORME UM NUMERO ENTRE 0 E 9999'))

while c<4:
   soma =  x // a % 10
   z = soma + z
   print('SOMA', z)
   a = a*10

   c = c + 1
   print('CONTROLE', c)

print('SOMA', z)