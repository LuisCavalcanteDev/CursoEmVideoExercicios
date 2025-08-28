# Exercicio anterenior: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = 0
soma_terceira_coluna = 0
maior_valor = 0

for linha in range(3):
    for coluna in range(3):
        print(f'[{linha} {coluna}]', end=' ')
        valor = int(input('Digite um valor: '))
        matriz[linha][coluna] = valor

        if valor % 2 == 0:
            par += valor

        if  coluna == 2:
            soma_terceira_coluna += valor

        if linha == 1 and valor > maior_valor:
            maior_valor = valor


print()



print('Matriz preenchida:')
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end='')
    print()

print(f'A soma dos valores pares é {par}')
print(f'A soma da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor é {maior_valor}')