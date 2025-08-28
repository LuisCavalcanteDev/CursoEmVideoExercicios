# Crie um programa que leia o nome completo de uma pessoa e mostre:
# * O nome com todas as letras maiúsculas e minúsculas.
# * Quantas letras ao todo (sem considerar espaços).
# * Quantas letras tem o primeiro nome.



nome = str(input('Digite seu nome:'))

nome_formatado_maiuscula = nome.upper()
nome_formatado_minuscula = nome.lower()
total_letras = int(len(nome.strip()) - nome.count(' '))
total_letras_primeironome = nome.split()
primeiro_nome = total_letras_primeironome[0]





print(f'Nome formatado para Maiúscula: {nome_formatado_maiuscula}')
print(f'Nome formatado para minúscula: {nome_formatado_minuscula}')
print(f'Quantidades de letras: {total_letras}')
print(f'Quantidades de letras no Primeiro nome: {len(primeiro_nome)}')
