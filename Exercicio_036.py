#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_da_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario: '))
qtde_anos = float(input('Digite o pagamentos em anos: '))

valor_do_salario_30 = salario * 30/100

valor_em_meses = valor_da_casa / (12 * qtde_anos)

print(f'O valor que você pode pagar no mês é R${valor_do_salario_30:.2f} e o valor minimo da parcela é: R${valor_em_meses:.2f}')


if valor_do_salario_30 < valor_em_meses:
    print(f'Infelizmente foi negado o emprestimo ')

else:
    print(f'O seu financiamento foi aprovado ')