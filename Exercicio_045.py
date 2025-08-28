#Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

jogador = str(input('''Escolha entre
PEDRA
PAPEL
TESOURA \n 
Digite aqui:''')).strip().upper()

maquina = choice(['PEDRA', 'PAPEL', 'TESOURA'])

if jogador == 'PEDRA' and maquina == 'PAPEL':
    print(f'Você escolheu {jogador} e o maquina {maquina}. \nVocê perdeu!!!')

elif jogador == 'PEDRA' and maquina == 'TESOURA':
    print(f'Você escolheu {jogador} e o maquina {maquina}. \nVocê ganhou!!!')

elif jogador == 'PAPEL' and maquina == 'PEDRA':
    print(f'Você escolheu {jogador} e o maquina {maquina}. \nVocê ganhou!!!')

elif jogador == 'PAPEL' and maquina == 'TESOURA':
    print(f'Você escolheu {jogador} e o maquina {maquina}. \nVocê perdeu!!!')

elif jogador == 'TESOURA' and maquina == 'PEDRA':
    print(f'Você escolheu {jogador} e o maquina {maquina}. \nVocê perdeu!!!')

elif jogador == 'TESOURA' and maquina == 'PAPEL':
    print(f'Você escolheu {jogador} e o maquina {maquina}. \nVocê ganhou!!!')

elif jogador ==  maquina :
    print(f'Você escolheu {jogador} e o maquina {maquina}. \nVocê EMPATOU!!!')
else:
    print('Escolha invalida!')