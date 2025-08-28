#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
numero = int(input('Qual número o computador pensou? 0 á 5: '))

lista = [0,1,2,3,4,5]
numero_do_computador = random.choice(lista)

if numero_do_computador == numero:
    print(f'O numero que computador escolheu foi {numero_do_computador} e o seu número é {numero} \nVocê ACERTOU!!!')
else:
    print(f'O numero que computador escolheu foi {numero_do_computador} e o seu número é {numero} \nVocê ERROU!!!')