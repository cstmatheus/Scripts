d = float(input('Distancia: '))

if d <= 200:
    t = d*0.50
    print('total a pagar {:.2f} por curta viagem'.format(t))
else:
    t = d * 0.45
    print('total a pagar {:.2f} por longa viagem'.format(t))