import math

m = 'CALCULA E MOSTRA'
print('\033[1;31m{:^40}\033[m'.format(m))
print('#'*40)
n1 = int(input('N1 ?'))
n2 = int(input('N2 ?'))
n3 = float(input('REAL ?'))
print('#'*40)
a = (n1 * 2) * (n2/2)

b = (n1 * 3) + n3

c = math.pow(n3, 3)

print('A {}\nB {}\nC {}'. format(a, b, c))
print('#'*40)