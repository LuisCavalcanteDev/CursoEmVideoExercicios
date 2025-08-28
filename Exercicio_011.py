#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura em metros:'))
altura = float(input('Digite a altura em metros:'))
m2 = largura * altura

litros = m2 / 2

input(f'A quantidade de litros de tinta para pintar a parede é: {litros:.3f}')