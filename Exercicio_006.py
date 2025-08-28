#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número:'))

dobro = numero * 2
triplo = numero * 3
raizquadrada = numero ** (1/2)

print(f'O número é: {numero}, o dobro é: {dobro}, o seu triplo é: {triplo} e a raiz quadrada é: {raizquadrada:.2f}')
