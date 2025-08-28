#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

valor1 =  int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))

if valor1 > valor2:
    print(f'O primeiro valor:{valor1} é maior que o segundo valor:{valor2}')
elif valor2 > valor1:
    print(f'O segundo valor:{valor2} é maior que o primeiro valor:{valor1}')
else:
    print(f'O primeiro valor:{valor1} e o segundo valor {valor2} são iguais' )