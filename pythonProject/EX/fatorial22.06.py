"""n = 1
while n > 0:
    n = int(input('VALOR'))
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1"""

x = 1
c = 1
n = 1

n = int(input('Digite o valor de n: '))

while n != 00:
    while c <= n:
        x *= c
        c += 1
        if n == 0:
            x = 1
    print(x)
    n = int(input('Digite o valor de n: '))