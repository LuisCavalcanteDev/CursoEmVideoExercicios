# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0,0,0], [0,0,0], [0,0,0]]

for linha in range(3):
    for coluna in range(3):
        print(f'[{linha} {coluna}]', end=' ')
        valor = int(input('Digite um valor: '))
        matriz[linha][coluna] = valor
print()



print('Matriz preenchida:')
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end='')
    print()