# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
lista = list()
contador = 0

for contador in range(0, 5):
    valor = int(input('Digite um valor: '))
    lista.append(valor)

maior = max(lista)
menor = min(lista)

print(f'O maior numero é {maior} nas posições ', end='')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f'{indice + 1}º.', end = '')

print()


print(f'O menor numero é {menor} nas posições ', end='')
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f' {indice + 1}º.', end='')