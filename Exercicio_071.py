#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

valor = int(input('Digite o valor que vc quer sacar? R$ '))
quantidade_notas_50 = quantidade_notas_20 = quantidade_notas_10 = quantidade_notas_01 = 0

while valor > 0:

    if valor >= 50:
        quantidade_notas_50 = valor // 50
        valor = valor % 50
    if valor < 50:
        quantidade_notas_20 = valor // 20
        valor = valor % 20
    if valor < 20:
        quantidade_notas_10 = valor // 10
        valor = valor % 10
    if valor < 10:
        quantidade_notas_01 = valor // 1
        break



print('-=*' * 30)


print(f'Quantidade de notas de 50:{quantidade_notas_50}')
print(f'Quantidade de notas de 20:{quantidade_notas_20}')
print(f'Quantidade de notas de 10:{quantidade_notas_10}')
print(f'Quantidade de notas de 01:{quantidade_notas_01}')


