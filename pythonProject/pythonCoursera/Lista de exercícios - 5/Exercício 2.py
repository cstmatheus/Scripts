largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

i = 0
c = 0
# ALT RECEBE A ALTURA MENOS A PRIMEIRA LINHA E A ULTIMA LINHA
alt = altura - 2

altura = altura - alt
# CONTROLA QUANTIDADE DE VEZES A APARICAO DOS CARACTERES
while i < altura:
    while c < largura:
        print('#', end = '')
        c += 1
    print()
    # SE CASO COLUNA > 2 ENTAO ELE MOSTRA AS LINHAS BRANCAS
    if c > 2:
        # MOSTRA AS LINHAS BRANCAS MENOS A PRIMEIRA LINHA E A ULTIMA LINHA
        while alt > 0:
            print('#' + (" " * (largura - 2)) + '#')
            alt -= 1

    i += 1
    c = 0