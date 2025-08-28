#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente


def ficha(nome= '<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s).')


nome = input('Digite o nome do jogador: ')
gols = input('Digite a quantidade de gols: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0


if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)