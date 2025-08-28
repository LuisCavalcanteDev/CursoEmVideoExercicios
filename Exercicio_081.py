#Crie um programa que vai ler vários números e colocar em uma lista.
#  Depois disso, mostre:
#    A) Quantos números foram digitados.
#    B) A lista de valores, ordenada de forma decrescente.
#    C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
numeros_digitados = 0

while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
    if continuar in 'Nn':
        break


print(f'--=--' * 30)
numeros_digitados = len(lista)
print(f'A quantidade de números digitados são: {numeros_digitados}')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista}')
lista.sort()
print(f'A lista em ordem descente é: {lista}')

if 5 in lista:
    print(f'O 5 está na {lista.index(5) + 1} posição')
else:
    print('Não tem o 5 na lista')