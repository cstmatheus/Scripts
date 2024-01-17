nome = str(input('Nome: ')).strip() #PEGANDO STRING CORTADA


print(nome.upper())  #NOME MAIUSCULO

print(nome.lower()) #NOME MINSCULO

print(len(nome) - nome.count(' ')) #CONTA O NOME SEM ESPACO

print(nome.replace(' ', ''))  # MOSTRA NOME SEM ESPACO TROCANDO UM ESPACO P/ UM VAZIO

#print(nome.find(' ')) #PESQUISA O PRIMEIRO ESPACO, PARA DIZER QUANTAS LETRAS HA NO 1 NOME

separa = nome.split()
print(separa[0], len(separa[0])) #DIVIDE O NOME COM O SPLIT, DPS CONTA A PARTIR DO INDICE 0 PARA MOSTRAR QTD DO 1 NOME