x = int(input('Digite o valor de n: '))

impar = 0
cont = 0

while cont < x:
    impar += 1

    if impar % 2 != 0:
        print(impar)
        #CONTROLA O LOOP
        cont += 1

