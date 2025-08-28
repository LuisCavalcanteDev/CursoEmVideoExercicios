#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

numero = 0
contador = 0
multiplicacao = 0


while numero >=0:
    numero = int(input('Digite um numero: '))

    if numero < 0:
        break
    else:
        contador = 0
        while contador < 10:
            multiplicacao = contador * numero
            print(f'{contador} X {numero} = {multiplicacao}')
            contador +=1


print('Fim do programa')