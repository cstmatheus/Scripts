import random

nome1 = input('Nome1: ')
nome2 = input('nome2: ')
nome3 = input('nome3: ')
nome4 = input('nome4: ')

lista = [nome1, nome2, nome3, nome4]

random.shuffle(lista)

#   r = random.choice(lista)



print(lista)