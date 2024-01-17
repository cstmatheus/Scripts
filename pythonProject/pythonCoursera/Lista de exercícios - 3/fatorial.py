n = int(input('Digite o valor de n: '))

x = 1
c = 1

while c <= n:
    #LOGICA DO FATORIAL
    x *= c
    #INCREMENTA OU SEJA SOMA MAIS UM NUMERO PARA A PROXIMA INTERACAO
    c += 1

    if n == 0:
        x = 1

print(x)


