#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.


lista_completa = [[], []]
contador = 1
while contador <= 7:
    numero = int(input(f'Digite o {contador} valor: '))
    if numero % 2 == 0:
        lista_completa[0].append(numero)
    else:
        lista_completa[1].append(numero)

    contador += 1

lista_completa[0].sort()
lista_completa[1].sort()

print(f'A lista completa dos pares {lista_completa[0]}')
print(f'A lista completa dos impares {lista_completa[1]}')
