def maior_primo(n):
    div = 1
    uau = True
    cont = 0
    while div <= n and uau:
        if n % div == 0:
            cont = cont+1
        if cont >= 3:
            cont = 1
            n = n - 1
            div = 1
        if cont == 2 and n == div:
             uau = False
        div = div + 1

    return n

maior_primo(7)