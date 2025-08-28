#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero  = int(input('Digite um número:'))

if numero % 2 == 0:
    print(f'O seu número {numero} é Par')
else:
    print(f'O numero {numero} que vc digitou é impar')
