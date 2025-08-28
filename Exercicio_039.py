# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))

ano_atual = date.today().year
verificador = ano_atual - ano



if verificador == 18:
    print(f'Você está no ano exato para o alistamento')
elif verificador < 18:
    anos_faltando = 18 - verificador
    ano_alistamento = ano_atual + anos_faltando
    print(f'Você ainda vai se alistar ')
    print(f'O ano de alistamento é: {ano_alistamento}')
else:
    print(f'Você passou do prazo para o alistamento')