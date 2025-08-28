# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a1 = int(input('Digite o primeiro número'))
a2 = int(input('Digite o segundo número'))
a3 = int(input('Digite o terceiro número'))

maior = max(a1, a2, a3)
menor = min(a1, a2, a3)

print(f'O menor valor é {menor} e o maior valor é {maior}  ')