# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

contador = 0
lista = []

while contador < 5:
    numero = int(input('Digite um número: '))

    if contador == 0:
        lista.append(numero)
    else:
        if lista[-1] < numero:
            lista.append(numero)
        else:
            for c in range(len(lista)):
                if numero <= lista[c]:
                    lista.insert(c, numero)
                    break

    print(lista)
    contador += 1
