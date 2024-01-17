largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

i = 0
c = 0

while i < altura:
    while c < largura:
        print('#', end='')
        c += 1
    print()
    i += 1
    c = 0


