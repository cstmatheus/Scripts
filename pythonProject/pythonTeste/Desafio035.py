print('-=-' * 10)
r1 = float(input('R1: '))
r2 = float(input('R2: '))
r3 = float(input('R3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1: # ANAÇLISE SE PODE FZER TRIANGULO
    print('Forma')
else:
    print('Nao forma')