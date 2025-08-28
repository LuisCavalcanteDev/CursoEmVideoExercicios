#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []

while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
    if continuar in 'Nn':
        break



for valor in lista:
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)

print(f'-=-' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de impares é {lista_impar}')
print(f'-=-' * 30)