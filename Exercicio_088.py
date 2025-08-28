#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
quantidade_de_jogos = int(input('Quantos jogos deseja gerar? '))
lista = []
jogo = []

while quantidade_de_jogos > 0:

    for valor in range(6):
        numero = randint(1, 60)
        while numero in jogo:
            numero = randint(1, 60)
        jogo.append(numero)



    jogo.sort()
    quantidade_de_jogos -= 1
    lista.append(jogo[:])
    jogo.clear()




for indice, valores in enumerate(lista):
    print(f'Jogo {indice + 1} - {valores}')
