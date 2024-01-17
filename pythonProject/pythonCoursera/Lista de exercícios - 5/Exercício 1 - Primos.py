def n_primos(n):
    z = n
    cont = 0
    i = 0

    verifica = 0
    conta = 1

    while i <= n or cont < 2:
        i = i + 1
        x = n % i
        if x == 0:
            cont = cont + 1

    if cont <= 2:
        aux = 0

    else:
        aux = 1
###

    while z > 0:
        primo = aux

        if primo == verifica:
            conta = conta + 1

        z = z - 1

        if z == 1:
            z = 0
    print(z)
    #return conta


n = int(input('DIGITE'))

n_primos(n)

print(n_primos(n))



