"""
18.	Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
 calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""


def velodown(tamArq, velocidade):
    tempo = float(tamArq / (velocidade / 8))
    minu = tempo / 60

    return print('A VELOCIDADE APROXIMADA E: [ {:^5} ] Mbps'.format(minu))


print('==' * 30)
m = 'tamanho de um arquivo para download (em MB): '
m = m.upper()
print('{}'.format(m))
tamArq = float(input())

print('==' * 30)
m = 'velocidade de um link de Internet '
m = m.upper()
print('{}(em Mbps) :'.format(m))
velocidade = float(input())
print('==' * 30)

print(velodown(tamArq, velocidade))
