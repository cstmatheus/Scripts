import math

n1 = float(input('Cat. oposto: '))

n2 = float(input('Cat. adj: '))

catop = math.pow(n1,2)

catadj  = math.pow(n2, 2)

hip = math.sqrt(catop + catadj)


print('hipo = {}, {}'.format(catop,catadj))

print ('{:.2f}'.format(hip))
