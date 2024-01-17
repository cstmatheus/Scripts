def fatorial(n):
    c = 1
    x = 1
    while c <= n:
        x *= c
        c += 1
        if n == 0:
            x = 1
    print(x)

n = 1

while n > 0:
    n = int(input('Digite o valor de n: '))
    fatorial(n)