#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = int(input('digite um angulo:'))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno tem o valor de :{seno:.3f}  \nO cosseno tem o valor de :{cosseno:.3f} \nA tangente tem o valor de :{tangente:.3f}')
