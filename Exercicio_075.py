#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite o ultimo valor: '))

tupla = (n1, n2, n3, n4)
quantidade_do_numero_9 = 0
quantidade_par = 0
posicao_3 = 0


for item in tupla:
    if item == 9:
        quantidade_do_numero_9 += 1

    if item % 2 == 0:
        quantidade_par += 1

    if item == 3:
        posicao_3 = tupla.index(item) + 1


print(f'Lista: {tupla}')
print(f'\nO número 9 apareceu: {quantidade_do_numero_9} vezes')
print(f'Posição do numero 3: {posicao_3}º')
print(f'Quantidade do numero par: {quantidade_par}')