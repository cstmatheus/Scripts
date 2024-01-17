lista2 = [10, 20, 30, 40, 50]
lista = [60, 70, 80, 90, 100]
x = 0

print('LISTA EXTENDIDA: ')
lista.extend(lista2)
print(lista)
print('=/'*30)

print('SORT REVERSE')
lista.sort(reverse=True)
print(lista)
print('=/'*30)

print('SORT')
lista.sort()
print(lista)
print('=/'*30)

print('SLICE/ FATIAMENTO MOSTRANDO ATE O 5 ELEMENTO')
print(lista[:5])

print('SLICE/ FATIAMENTO MOSTRANDO DO 5 ELEMENTO EM DIANTE')
print(lista[5:])

print('MIN')
print(min(lista))
print('=/'*30)

print('MAX ')
print(max(lista))
print('=/'*30)

print('SOMATORIA: ')
print(sum(lista))
print('=/'*30)

print('TAMANHO - LEN')
print(len(lista))
print('=/'*30)


print('QUANTOS VALORES IGUAL AO DO CRITERIO')
print('\n',lista.count(10))
print('=/'*30)



print('ENUMERATE: ')
for indice, valor in enumerate(lista):
    print(indice, valor)
print('=/'*30)

