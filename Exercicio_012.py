#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

valor = float(input('Digite o valor do produto:'))
valor_com_desconto = valor - (valor * 0.05)

print(f'O valor R${valor} com 5% de desconto é: R${valor_com_desconto:.2f}')