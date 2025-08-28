#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite o primeiro lado do triangulo: '))
b = float(input('Digite o segundo lado do triangulo: '))
c = float(input('Digite o terceiro lado do triangulo: '))

if a + b > c and a + c > b and b + c > a:
    print('Essas medidas podem formar um triângulo')
else:
    print('Não tem como formar um triângulo')