#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)


contador = 0
soma = 0
while True:

    numero = int(input('Digite um numero: '))

    if numero == 999:
        break
    soma = soma + numero
    contador += 1
print(f'Foi digitado {contador} numeros e o valor da soma é {soma}')