#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
contador = 0

while True:
    numero_jogador = int(input('Digite um numero: '))
    numero = randint(0, 10)
    escolha = str(input('Par ou impar? [P/I] ')).upper().strip()[0]

    if escolha == 'P':
        if (numero_jogador + numero) % 2 == 0:
            print('--' * 30)
            print(f'O numero que você jogou foi {numero_jogador} e a maquina foi {numero}  \nA soma foi: {numero_jogador + numero} \nVocê ganhou!!!')
            print('--' * 30)
            contador += 1
        else:
            print('--' * 30)
            print(f'Você perdeu com {contador} vitorias. \nO numero da maquina foi {numero} \nA soma foi: {numero_jogador + numero}')
            print('--' * 30)
            break

    if escolha == 'I':
        if (numero_jogador + numero) % 2 == 0:
            print('--' * 30)
            print(f'Você perdeu com {contador} vitorias. \nO numero da maquina foi { numero} \nA soma foi: {numero_jogador + numero}')
            print('--' * 30)
            break
        else:
            print('--' * 30)
            print(f'O numero que você jogou foi {numero_jogador} e a maquina foi {numero} \nA soma foi: {numero_jogador + numero} \nVocê ganhou!!!')
            print('--' * 30)
            contador += 1
