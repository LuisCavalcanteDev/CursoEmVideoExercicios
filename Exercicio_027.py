#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome  = str(input('Digite seu nome: ')).strip()

nome_separado = nome.split()

print(f'O primeiro nome da pessoa é: {nome_separado[0]} e o último nome da pessoa é: {nome_separado[-1]}')

