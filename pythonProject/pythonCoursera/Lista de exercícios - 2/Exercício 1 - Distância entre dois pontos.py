import math

x = float(input('x: '))
y = float(input('y: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))

d = math.sqrt((x - x2)**2 + (y - y2)**2)

if d >= 10:
    print('longe')
else:
    print('perto')