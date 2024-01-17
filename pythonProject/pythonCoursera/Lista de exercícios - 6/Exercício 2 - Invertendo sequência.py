"""
Como pedido na primeira video-aula desta semana, escreva um programa que recebe
uma sequência de números inteiros e imprima todos os valores em ordem inversa.
A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.

"""
lista = []

x = int(input('Digite um número:'))
while x > 0:

    lista.append(x)

    x = int(input('Digite um número:'))

lista.reverse()
for i in range(len(lista)):
    print(lista[i])