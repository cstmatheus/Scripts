n = int(input('Numero: '))

v = n%3
v1 = n%5

if v==0 and v1==0:
    print('FizzBuzz')
else:
    print(n)
