#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


dicionario =  {}
lista_gols_por_partidas = []
total_de_gols = 0

nome = str(input('Digite o nome do jogador: '))
quantidade_partidas = int(input('Digite a quantidade de partidas: '))
print('=-' * 30)

dicionario['Nome'] = nome
for partida in range(1, quantidade_partidas + 1):
    quantidade_gol = int(input(f'Na {partida} ele fez quantos gols: '))
    lista_gols_por_partidas.append((partida, quantidade_gol))
    total_de_gols += quantidade_gol

dicionario['Total de gols'] = total_de_gols
dicionario['Quantidade Partidas'] = quantidade_partidas

dicionario['lista_gols_por_partidas'] = lista_gols_por_partidas[:]
print('=-' * 30)

for chave, valor in dicionario.items():
    if chave == 'lista_gols_por_partidas':
        for partida, quantidade_gol in lista_gols_por_partidas:
            print(f' => Na {partida}º ele fez {quantidade_gol} gols.')
    else:
        print(f'{chave} = {valor}')

print('=-' * 30)






