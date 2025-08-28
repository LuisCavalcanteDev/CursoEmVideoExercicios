#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = []

# Cadastro dos alunos
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    alunos.append([nome, nota1, nota2, media])

    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break


print('-=' * 30)
print(f'{"Nº":<4}{"Nome":<15}{"Média":>8}')
print('-' * 30)

for indice, aluno in enumerate(alunos):
    print(f'{indice:<4}{aluno[0]:<15}{aluno[3]:>8.1f}')

while True:
    selecionar = int(input('Digite o número do aluno para ver as notas [999 para sair]: '))

    if selecionar == 999:
        print('Encerrando consulta de notas...')
        break

    if 0 <= selecionar < len(alunos):
        print('-' * 30)
        print(f'As notas de {alunos[selecionar][0]} são: {alunos[selecionar][1]} e {alunos[selecionar][2]}')
        print('-' * 30)
    else:
        print('Número inválido. Tente novamente.')
