n1 = int(input('N1'))

n2 = int(input('N2'))

n3 = int(input('N3'))

if(n1 > n2):
    if(n1 > n3):
        print('n1 MAIOR E O {}'.format(n1))

if(n2 > n1):
    if(n2 > n3):
        print('n2 MAIOR E O {}'.format(n2))

if(n3 > n1):
    if(n3 > n2):
        print('n3 MAIOR E O {}'.format(n3))

#################

if (n1 < n2):
     if (n1 < n3):
         print('n1 MENOR E O {}'.format(n1))

if (n2 < n1):
     if (n2 < n3):
          print('n2 MENOR E O {}'.format(n2))

if (n3 < n1):
     if (n3 < n2):
           print('n3 MENOR E O {}'.format(n3))