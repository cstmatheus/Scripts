n = int(input("Digite um numero: "))

ant = n % 10
n = n // 10
adj_iguais = False
dps = 0

while n > 0 and not adj_iguais:
    at = n % 10
    if at == ant:
        adj_iguais = True
    else:
        dps += 1
    ant = at
    n = n // 10

if adj_iguais:
    print('sim')
else:
    print('não')