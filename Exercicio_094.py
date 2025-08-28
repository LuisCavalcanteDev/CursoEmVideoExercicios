#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

lista_pessoas = []
dicionario_pessoa = {}

media_idade = 0
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    idade = int(input('Idade: '))

    dicionario_pessoa['Nome'] = nome
    dicionario_pessoa['Sexo'] = sexo
    dicionario_pessoa['Idade'] = idade

    lista_pessoas.append(dicionario_pessoa.copy())
    dicionario_pessoa.clear()

    continuar = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break


for valor in lista_pessoas:
    media_idade = (valor['Idade'] + media_idade)

quantidade = len(lista_pessoas)
media_idade = media_idade / quantidade

print('=-' * 30)
print(f'Foi cadastrado {len(lista_pessoas)} pessoas.')
print(f'A média da idade é {media_idade:.2f} anos.')

print('As mulheres cadastradas foram: ', end='')
for valor in lista_pessoas:
    if valor['Sexo'] == 'F':
        print(f'(Nome: {valor["Nome"]}  Idade: {valor["Idade"]} e Sexo: {valor["Sexo"]} ) |', end ='' )

print()
print('Quantidade de pessoas acima da media da idade:', end='')

for valor in lista_pessoas:
    if valor['Idade'] > media_idade:
        print(f'(Nome: {valor["Nome"]}  Idade: {valor["Idade"]} e Sexo: {valor["Sexo"]} ) | ', end='')

print()
print('=-' * 30)
