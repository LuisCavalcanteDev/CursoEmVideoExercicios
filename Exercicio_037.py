#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero =  int(input('Digite um número para conversão: '))

print(''' Escolha qual tipo você quer converter
          1 - Binário
          2 - Octal 
          3 - Hexadecimal   ''')
escolha = int(input(':'))
if escolha == 1:
    print(f'O numero {numero} convertido para binario é:{bin(numero)[2:]} ')
elif escolha == 2:
    print(f'O numero {numero} convertido para octal é:{oct(numero)[2:]} ')
elif escolha == 3:
    print(f'O numero convertido para hexadecimal:{hex(numero)[2:]}12')
else:
    print('Opcção invalida')
