#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~


frase = str(input('Digite uma frase: ')).strip()

def escreva(frase):
    print('~' * (len(frase ) + 2))
    print(f' {frase}')
    print('~' * (len(frase) + 2))

escreva(frase)