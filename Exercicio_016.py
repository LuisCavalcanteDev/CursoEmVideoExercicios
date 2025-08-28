#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
numero = float(input('Digite um número real'))

print(f'O numero é {numero} e sua porção inteira é {numero:.0f}')


# Outro maneira de fazer usando o modulo math

print(f'O numero é {numero} e sua porção inteira é {math.trunc(numero)}')