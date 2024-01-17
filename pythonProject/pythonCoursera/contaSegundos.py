"""OPCAO 1

a linguagem de programação é python, eu fiz desse jeito

seg = int(input("Digite os segundos: "))


a = seg//60//60//24
b = (seg//60//60)%24
c = (seg//60)%60
d = seg%60

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")

################OPCAO 2
 Acredito que a logica é a mesma para qualquer linguagem.Fiz um programinha em C++ usando funções, ficou mais ou menos assim.

{
    while(totalsegundos>=86400)
   {
        totalsegundos-=86400;
        dia++;
   }
    while(totalsegundos>=3600)
    {
        totalsegundos-=3600;
        hora++;
    }

    while(totalsegundos>=60)
    {
        totalsegundos-=60;
        minutos++;
    }

    cout << dia << " : " << hora << " : " << minutos << " : " << totalsegundos << endl;           // cout é o mesmo que printf em C
}
"""

s = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dia = s//60//60//24
hora = (s//60//60)%24
segRes = s % 3600
minuto = segRes // 60
segResF = segRes % 60

print('{:.0f} dias, {} horas, {} minutos e {} segundos.'.format(dia, hora, minuto, segResF))