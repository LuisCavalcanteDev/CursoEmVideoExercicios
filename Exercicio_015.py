# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

km_rodados = float(input('Quantos Km você rodou: '))
dias = int(input('Em quantos dias:'))

valor_a_pagar = (dias * 60) + (km_rodados * 0.15)

print(f'O valor que precisa ser pago é R${valor_a_pagar:.2f}')