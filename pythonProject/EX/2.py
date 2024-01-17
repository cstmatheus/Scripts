print('#######SISTEMA BANCO#######')

senha = int(input('DIGITE A SENHA: '))

conta = 0

while (conta<2):
    conta=conta+1
    if(senha == 19):

        a = int(input('DIGITE 1 PARA ENTRAR ACESSAR A CONTA'))

        while (a == 1):

            conta = int(input('DIGITE A SUA CONTA: '))

            saldo = int(input('DIGITE SEU SALDO: '))

            op = int(input('(1) PARA DEPOSITAR'
                           '(2) PARA SACAR'))

            valor = int(input('DIGITE O VALOR: '))

            if(op==1):
                saldo = saldo + valor

            elif(op==2):
                if(saldo<valor):
                    print('saldo insuficiente!')
                    saldo = saldo - valor

            print('SEU SALDO ATUAL DA CONTA: {} E: {} reais'.format(conta, saldo))

            a = int(input('DIGITE 1 PARA CONTINUAR'))


    else:
        print('SENHA ERRADA')
        senha = int(input('DIGITE A SENHA: '))

