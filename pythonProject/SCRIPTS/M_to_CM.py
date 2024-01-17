"""
5.	Faça um Programa que converta metros para centímetros
"""

m = '[1] METROS(M) PARA CENTIMETROS(CM)\n[2] CENTIMETROS(CM) PARA METROS(M)'

print('DIGITE: ')
print(f'\n{m}\n')
print('=*'*30)
op = int(input())
print('=*' * 30)
#print('\n')
if (op == 1):

    m = float(input('METROS: '))
    print('=*'*30)
    con = m * 100

    print(f'[{m:.2f}] METROS\nEQUIVALE A [{con:.2f}] CENTIMETROS')


elif (op == 2):

    cm = float(input('CENTIMETROS: '))

    con = cm / 100
    print(f'[{cm:.2f}] CENTIMETROS\nEQUIVALE A [{con:.2f}] METROS')
