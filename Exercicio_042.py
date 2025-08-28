#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes


#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite o primeiro lado do triangulo: '))
b = float(input('Digite o segundo lado do triangulo: '))
c = float(input('Digite o terceiro lado do triangulo: '))

if a + b > c and a + c > b and b + c > a:
    print('Essas medidas podem formar um triângulo')
    if a == b and a == c:
        print('Esse é um triângulo equilátero')
    elif a == b or a == c or b == c:
        print('Esse é um triângulo isósceles')
    elif a != b and a != c and b != c:
        print('Esse é um triângulo escaleno')
else:
    print('Não tem como formar um triângulo')