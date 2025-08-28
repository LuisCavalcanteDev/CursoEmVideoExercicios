#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    numero = int(input('Digite um numero: '))
    if numero not in lista:
        lista.append(numero)

    else:
        print('Número duplicado, não será adicionado ...')


    continuar = input('Deseja continuar? [S/N] ')
    if continuar in 'Nn':
        break

lista.sort()
print(f'Esta é a lista final: {lista}')
