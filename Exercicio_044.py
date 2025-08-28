# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros


valor_do_produto = float(input('Digite o valor do produto: '))

codicao_pagamento = int(input('''Digite a condição de pagamento: 
                               1 - À vista dinheiro/cheque
                               2 - À vista no cartão
                               3 - em até 2x no cartão
                               4 - 3x ou mais no cartão \n :''' ))

if codicao_pagamento == 1:
    novo_valor = valor_do_produto - valor_do_produto * (10/100)
    print(f'O valor do produto é: {novo_valor:.2f}')
elif codicao_pagamento == 2:
    novo_valor = valor_do_produto - valor_do_produto * (5/100)
    print(f'O valor do produto é: {novo_valor:.2f}')
elif codicao_pagamento == 3:
    print(f'O valor do produto é: {valor_do_produto:.2f}')
elif codicao_pagamento == 4:
    novo_valor = valor_do_produto + valor_do_produto * (20/100)
    print(f'O valor do produto é: {novo_valor:.2f}')
else:
    print('Você não escolheu uma opçao correta')


