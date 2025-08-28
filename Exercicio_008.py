#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Dgite um valor em metros:"))

centimetros = metros * 100
milimetros = metros * 1000

print(f'O valor digitado foi: {metros} ele em centimetros é: {centimetros} e em milimetros é: {milimetros}')