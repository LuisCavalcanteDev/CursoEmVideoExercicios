#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o salario: "))

if salario <= 1250:
    novo_salario = salario + (salario * 0.15)
    print(f'Você teve um aumento de 15% no seu salario de R${salario:.2f} e seu novo valor é: R$ {novo_salario:.2f}')
else:
    novo_salario = salario + (salario * 0.10)
    print(f'Você teve um aumento de 10% no seu salario de R${salario:.2f} e seu novo valor é: R$ {novo_salario:.2f}')