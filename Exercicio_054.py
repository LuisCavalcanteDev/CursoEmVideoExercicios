# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores de 21 anos.

from datetime import date

data_atual = date.today().year

numero_pessoa = 1
qtde_maioridade = 0
qtde_menoridade = 0

for contador in range(1,8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {numero_pessoa}ª :'))
    numero_pessoa += 1
    idade = data_atual - ano_nascimento
    if idade >= 21:
        qtde_maioridade += 1
    else:
        qtde_menoridade += 1

print(f'Temos {qtde_maioridade} na maioridade e temos {qtde_menoridade} 200na menoridade')
