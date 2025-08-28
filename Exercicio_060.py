#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

numero = int(input('Digite um valor para ver o seu fatorial:'))
multiplicacao = 1
print(f'{numero}! = ', end='')

while numero > 0:
    print(f' {numero}', end = ' ')
    if numero != 1:
        print(f'x', end='')
    if numero > 0:
        multiplicacao = multiplicacao * numero

    numero = numero - 1


print(f' =  {multiplicacao}')