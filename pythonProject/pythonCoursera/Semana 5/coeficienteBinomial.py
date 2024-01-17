def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

def numeroBinomial (n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

def testaFatorial():
    if fatorial(1) == 1:
        print('Funciona para 1')
    else:
        print('Não funciona para 1')
    if fatorial(2) == 2:
        print('Funciona para 2')
    else:
        print('Não funciona para 2')
    if fatorial(0) == 1:
        print('Funciona para 0')
    else:
        print('Não funciona para 0')
    if fatorial(5) == 120:
        print('Funciona para 5')
    else:
        print('Não funciona para 5')

def testeBinomial():
    if numeroBinomial(7, 3) == 35:
        print('Funciona para 7 sobre 3')
    else:
        print('Não funciona para 35')
    if numeroBinomial(10, 6) == 210:
        print('Funciona para 10 sobre 6')
    else:
        print('Não funciona para 10 sobre 6')

testeBinomial()

#print(numeroBinomial(10, 6))
#testaFatorial()