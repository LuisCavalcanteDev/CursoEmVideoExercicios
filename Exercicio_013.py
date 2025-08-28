#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do seu salario: R$'))

novo_salario =  salario + (salario * 0.15)

print(f'Seu novo salario é: R${novo_salario:.2f}')