#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.


dinheiro = float(input('Digite o valor em reais para converter para dolar:'))

dolar = dinheiro / 5.66

print(f'O valor {dinheiro} convertido em dolar é {dolar:.2f}')