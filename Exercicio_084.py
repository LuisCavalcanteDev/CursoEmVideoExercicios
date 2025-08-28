#Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pesado = 0
leve = 0

lista_pessoas = []
pessoas = []
while True:

    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))



    if len(lista_pessoas) == 0:
        pesado = pessoas[1]
        leve = pessoas[1]
    else:
        if  pesado <  pessoas[1]:
            pesado = pessoas[1]
        if leve > pessoas[1]:
            leve = pessoas[1]

    lista_pessoas.append(pessoas[:])
    pessoas.clear()

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break


print('-=' * 30)
print(f'A sua lista tem {len(lista_pessoas)} pessoas. ')
print('-=' * 30)
print(f'O maior peso foi: {pesado}.Os nomes :', end = '')
for pessoa in lista_pessoas:
    if pessoa[1] == pesado:
        print(f'|{pessoa[0]}|', end = '')
print()
print('-=' * 30)


print(f'O menor peso foi: {leve}.Os nomes:', end = '')
for pessoa in lista_pessoas:
    if pessoa[1] == leve:
        print(f'|{pessoa[0]}|', end = '')

print()
print('-=' * 30)

