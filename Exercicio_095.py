#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


lista_jogadores = []

while True:
    dicionario = {}
    lista_gols_por_partidas = []
    total_de_gols = 0

    nome = str(input('Digite o nome do jogador: '))
    quantidade_partidas = int(input('Digite a quantidade de partidas: '))
    print('=-' * 30)

    for partida in range(1, quantidade_partidas + 1):
        quantidade_gol = int(input(f'Na {partida}ª partida ele fez quantos gols? '))
        lista_gols_por_partidas.append((partida, quantidade_gol))
        total_de_gols += quantidade_gol

    dicionario['Nome'] = nome
    dicionario['Quantidade Partidas'] = quantidade_partidas
    dicionario['Total de gols'] = total_de_gols
    dicionario['lista_gols_por_partidas'] = lista_gols_por_partidas[:]

    lista_jogadores.append(dicionario.copy())

    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    print('=-' * 30)

print('=-' * 30)
print(f'{"Cód":<5}{"Nome":<15}{"Total de Gols":<15}')
print('-' * 35)
for index, jogador in enumerate(lista_jogadores):
    print(f'{index:<5}{jogador["Nome"]:<15}{jogador["Total de gols"]:<15}')
print('=-' * 30)


while True:
    resposta = input('Qual jogador quer ver os dados? [999 para sair] ')
    if resposta == '999':
        break
    if not resposta.isdigit():
        print('Por favor, digite um número válido.')
        continue

    codigo = int(resposta)
    if codigo < 0 or codigo >= len(lista_jogadores):
        print('Código inválido. Tente novamente.')
    else:
        jogador = lista_jogadores[codigo]
        print(f'\n-- LEVANTAMENTO DO JOGADOR {jogador["Nome"]} --')
        for partida, gols in jogador['lista_gols_por_partidas']:
            print(f'  Na {partida}ª partida fez {gols} gols.')
        print('=-' * 30)


