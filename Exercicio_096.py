#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def área(x, y):
    area = largura * altura

    print(f'A area de {x} x {y} é {area}')


largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

área(largura, altura)
