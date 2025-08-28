#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):

    while True:
        valor = input(msg)
        if valor.isnumeric():

            return int(valor)

        else:
            print('Você não digitou um número: ')

n = leiaInt('Digite um número')
print(f'Você acabou de digitar o número {n}')