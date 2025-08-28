#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
cateto_oposto = float(input('Digite o valor do cateto oposto:'))
cateto_adjacente = float(input('Digite o valor do cateto adjacente:'))

hipotenusa = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** (1/2)
print(f'A hipotenusa tem o valor de {hipotenusa} ')





#Outro jeito com math com o modulo math

hipotenusa2 = math.hypot(cateto_oposto , cateto_adjacente )

print(f'Valor com o math {hipotenusa2}')