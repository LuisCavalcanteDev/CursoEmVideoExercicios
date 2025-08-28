#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):

    while True:
        valor = input(msg)

        try:
            valor = int(valor)

        except:
            print('\033[031mDeu algum erro, Tente novamente!\033[m')

        else:
            return valor

def leiaFloat(msg):

    while True:
        valor = input(msg)

        try:
            valor = float(valor)


        except:
            print('\033[031mDeu algum erro, Tente novamente!\033[m')

        else:
            return valor

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
