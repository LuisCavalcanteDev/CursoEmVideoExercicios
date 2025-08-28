# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER


from datetime import date
ano = int(input('Digite o ano que você nasceu: '))

ano_atual = date.today().year

idade = ano_atual - ano

print(f'O atleta tem {idade} anos')
if idade <=9:
    print('Você esta na categoria: MIRIM')
elif idade <= 14:
    print('Você esta na categoria: INFANTIL')
elif idade <= 19:
    print('Você esta na categoria: JÚNIOR')
elif idade <= 25:
    print('Você esta na categoria: SÊNIOR')
elif idade > 25:
    print('Você esta na categoria: MASTER')