#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


peso_maior = 0
peso_menor = 0

for contador in range(1, 6):
    peso = float(input(f'Digite o peso da {contador}ª pessoa (em kg): '))

    if contador == 1:

        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso

print(f'\nMaior peso lido: {peso_maior} kg')
print(f'Menor peso lido: {peso_menor} kg')
