# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

contagem = 0
numero =  int(input('Digite um numero: '))

for contador in range(1, numero + 1):
    if numero % contador == 0:
        contagem += 1

if contagem > 2:
    print('O número não é primo')
else:
    print('O número é primo')