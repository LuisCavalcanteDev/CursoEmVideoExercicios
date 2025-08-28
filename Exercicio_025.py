#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome: ')).strip()

comparacao = 'SILVA' in nome.upper()
print(f'O nome da pessoa tem silva? {comparacao}')