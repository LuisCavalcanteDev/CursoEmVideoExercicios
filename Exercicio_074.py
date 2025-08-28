# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


import random

tupla = ( random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),)
maior = 0
menor = 0
for numero in tupla:
    print(numero, end=' ')
    if numero == tupla[0]:
        menor = numero
        maior = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

print(f'\nMenor valor é: {menor}')
print(f'Maior valor é: {maior}')

