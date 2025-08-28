#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa



primeiro_numero = float(input('Digite o primeoro número: '))
segundo_numero  = float(input('Digite o segundo numero: '))
operacao = 0

while operacao != 5:
    operacao = int(input('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
:'''))
    if operacao == 1:
        valor = primeiro_numero + segundo_numero
        print('|||||||||||||||||||||||')
        print(f'A soma {primeiro_numero} + {segundo_numero} é {valor}')
        print('|||||||||||||||||||||||')

    elif operacao == 2:
        valor = primeiro_numero * segundo_numero
        print('|||||||||||||||||||||||')
        print(f'A multiplicação {primeiro_numero} x {segundo_numero} é {valor}')
        print('|||||||||||||||||||||||')

    elif operacao == 3:
        if primeiro_numero > segundo_numero:
            print('|||||||||||||||||||||||')
            print(f'O maior valor entre o {primeiro_numero} e o {segundo_numero} é {primeiro_numero}')
            print('|||||||||||||||||||||||')

        else:
            print('|||||||||||||||||||||||')
            print(f'O maior valor entre o {primeiro_numero}  e o {segundo_numero} é {segundo_numero}')
            print('|||||||||||||||||||||||')

    elif operacao == 4:
        print('Digite novamente os valores')
        primeiro_numero = float(input('Digite o primeoro número: '))
        segundo_numero = float(input('Digite o segundo numero'))



print('Muito obrigador por usar o nosso programa')