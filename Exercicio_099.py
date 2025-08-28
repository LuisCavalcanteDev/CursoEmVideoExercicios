#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.



def maior(*valor):
    print(f'Analisando os valores passados...')
    print(f'{valor}')
    maior_valor = max(valor)
    print(f'O maior valor é {maior_valor}')
    print('=-' * 30)




maior(1,5,6,7,810,669,556)

maior(1588,1556,111,1666,5444,258)
maior(1588,1,111,1666,13,258)