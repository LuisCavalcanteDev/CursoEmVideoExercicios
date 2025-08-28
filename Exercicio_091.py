# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint



dicionario = {  'jogador1' : randint(1, 6),
                'jogador2' : randint(1, 6),
                'jogador3' : randint(1, 6),
                'jogador4' : randint(1, 6)
            }

for key, value in dicionario.items():
    print(f'{key} tirou {value}')

ranking = dicionario.items()
ranking = sorted(ranking, key = lambda valor: valor[1], reverse = True)

print('=-' * 30)


for posicao, (jogador, numero) in enumerate(ranking, start=1):
    print(f'{posicao}º lugar: {jogador} tirou {numero}')
print('=-' * 30)