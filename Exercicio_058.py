#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
numero = int(input('Qual número o computador pensou? 0 á 10: '))

lista = [0,1,2,3,4,5,6,7,8,9,10]
numero_do_computador = random.choice(lista)
qtde = 0

while numero_do_computador != numero:
    numero = int(input('Você errou, escolha outro número entre 0 á 10: '))
    qtde += 1

print(f'Você acertou! em {qtde} tentativas')
print(f'O numero que o computador pensou foi {numero_do_computador}')
