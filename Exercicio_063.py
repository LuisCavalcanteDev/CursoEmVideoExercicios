#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

termos = int(input('Quantos termos você quer? '))

anterior = 0
posterior = 1

contador = 0

while contador < termos:
    print(anterior, end=' -> ')
    soma = anterior + posterior
    anterior = posterior
    posterior = soma
    contador += 1

print('FIM')
