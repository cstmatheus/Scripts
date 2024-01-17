def primo(n):
    cont = 0
    i = 0
    v = False
    while i <= n or cont < 2:
        i = i + 1
        x = n % i
        if x == 0:
            cont = cont + 1

    if cont <= 2:
         v = True
         return v
    else:
        return v

n = 1

while n > 0:
    n = int(input("Digite um número inteiro: "))
    print(primo(n))