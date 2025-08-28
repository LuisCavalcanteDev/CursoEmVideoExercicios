#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for contador in range(1,501):
    if contador % 3 == 0:
        soma = contador + soma
print(soma, end=' ')
print('\n FIM DO PROGRAMA')