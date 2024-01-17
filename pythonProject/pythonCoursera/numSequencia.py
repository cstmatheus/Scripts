adjacente = 'False'
posterior = -1

n = int(input('INFORME UM NUMERO: '))

while n != 0:
    anterior = posterior
    posterior = n % 10
    print('anterior = {}\nPOSTERIOR = {}'.format(anterior, posterior))
    print(adjacente)

    if anterior == posterior:
        adjacente = 'True'
        n = 0
        n = n / 10
        print('DENTRO DO IF anterior = {}\nPOSTERIOR = {}'.format(anterior, posterior))

"""if adjacente=='False':
    print("NAO\n")
else:
    print("SIM\n")"""