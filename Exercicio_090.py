#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dicionario = {}
nome = str(input('Nome do aluno: '))
media = float(input('Media do aluno: '))
situacao = ''
if media >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'


dicionario['nome'] = nome
dicionario['media'] = media
dicionario['situacao'] = situacao

print('=-' * 30)
print(f'O aluno {dicionario["nome"]} ficou com a média de {dicionario["media"]}')
print(f'{dicionario["situacao"]}')
print('=-' * 30)