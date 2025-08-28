#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. 40 anos de contribuição

from datetime import date

dicionario = dict()
ano_atual = date.today().year

nome = input('Digite o nome do aluno: ')
ano_nascimento = int(input('Digite o ano de nascimento: '))
ctps = int(input('Digite o código da Carteira de trabalho [Se não tiver, digite 0]: '))

dicionario['nome'] = nome
dicionario['ano_nascimento'] = ano_nascimento
dicionario['idade'] = ano_atual - ano_nascimento

if ctps == 0:
    dicionario['ctps'] = 0
else:
    ano_contratacao = int(input('Digite o ano de contratação: '))
    salario = float(input('Digite o salário: '))

    dicionario['ctps'] = ctps
    dicionario['ano_contratacao'] = ano_contratacao
    dicionario['salario'] = salario

    ano_aposentadoria = ano_contratacao + 40
    dicionario['ano_aposentadoria'] = ano_aposentadoria

print('=-' * 30)
for chave, valor in dicionario.items():
    print(f'{chave.capitalize()}: {valor}')
print('=-' * 30)
