#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


numero = int(input('Digite um  numero inteiro:'))

continuar = True
soma = 0
maior = 0
menor = 0
contador = 0
media = 0

while continuar == True:
    soma += numero

    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if contador == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    if opcao == 'S':
        numero = int(input('Digite um  numero inteiro:'))
        continuar = True
    else:
        continuar = False

    contador += 1
    media = soma / contador


print(f'O maior numero foi {maior} e o menor foi {menor} e a media foi {media}')
print('Fim do programa')



