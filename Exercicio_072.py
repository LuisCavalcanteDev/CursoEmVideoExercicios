#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.



tupla =  ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez','onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')


while True:
    numero = int(input('Digite um número para mostrar ele por extenso: [entre 0 e 20]: '))
    if 0 <= numero <= 20:
        break

print(f'O numero por extenso é: {tupla[numero]}')