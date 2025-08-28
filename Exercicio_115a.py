#: Vamos criar um menu em Python, usando modularização,
#   Não coloquei em modularização, pois cria muitas pastas e acaba confundindo na hora de ver os exercicios prontos, como são exercicios não vejo problema, mas a idédia é criar uma pasta e colocar as def lá
c = {
'limpa': '\033[m',
'preto': '\033[30m',
'vermelho': '\033[31m',
'verde': '\033[32m',
'amarelo': '\033[33m',
'azul': '\033[34m',
'magenta': '\033[35m',
'ciano': '\033[36m',
'branco': '\033[37m'
    }


def leiaInt(msg):

    while True:
        valor = input(msg)

        try:
            valor = int(valor)

        except:
            print('\033[031mDeu algum erro, Tente novamente!\033[m')

        else:
            return valor


def opcao1():
    print('-' * 50)
    print(f'{c['verde']}{"OPÇÃO 1":^50}{c["limpa"]}')



def opcao2():
    print('-' * 50)
    print(f'{c['verde']}{"OPÇÃO 2":^50}{c["limpa"]}')


def opcao3():
    print('-' * 50)
    print(f'{c['vermelho']}{"SAINDO DO SISTEMA":^50}{c["limpa"]}')



def menu():
    print('-' * 50)
    print(f'{c["magenta"]}{"MENU PRINCIPAL":^50} {c["limpa"]}')
    print('-' * 50)

    print(f'1 -{c["azul"]} Para ver pessoas cadastradas{c["limpa"]}')
    print(f'2 -{c["azul"]} Cadastrar novas pessoas{c["limpa"]}')
    print(f'3 -{c["azul"]} Sair do sistema{c["limpa"]}')
    print(f'-' * 50)


while True:
    menu()
    opcao = leiaInt('Digite a sua opção:')

    if opcao == 1:
        opcao1()


    elif opcao == 2:
        opcao2()



    elif opcao == 3:
        opcao3()


        break

    else:
        print(f'{c["vermelho"]}Digite um numero entre as OPÇÕES:{c["limpa"]}')



