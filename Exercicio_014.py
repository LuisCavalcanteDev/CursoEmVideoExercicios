#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

celsius = float(input('Escreva a tesperatura em graus Celsius:'))

fahrenheit = (celsius * 1.8) + 32

print(f'A temperatura em graus fahrenheit é {fahrenheit:.2f}')