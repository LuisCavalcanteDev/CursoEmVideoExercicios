#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
for contador in range(1,7):
    numero = int(input(f'Digite o {contador} numero: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos numeros pares é: {soma}')
