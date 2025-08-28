# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = maior1000 = contador = preco_mais_barato = 0
nome_produto_mais_barato = ''


while True:
    print('-=' * 30)
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o valor do produto: R$ '))
    print('-=' * 30)

    total += preco
    contador += 1

    if preco > 1000:
        maior1000 += 1

    if contador == 1:
        nome_produto_mais_barato = nome
        preco_mais_barato = preco
    else:
        if preco_mais_barato > preco:
            preco_mais_barato = preco
            nome_produto_mais_barato = nome



    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' *30)
print(f'O total da compra foi R$ {total:.2f}')
print(f'A quantidade de produtos que custam mais que R$ 1000 : {maior1000}.')
print(f'O produto mais barato foi o {nome_produto_mais_barato} e custa R$ {preco_mais_barato:.2f}')
