#  Não coloquei em modularização, pois cria muitas pastas e acaba confundindo na hora de ver os exercicios prontos, como são exercicios não vejo problema, mas a idédia é criar uma pasta e colocar as def lá
# Vamos finalizar o projeto de acesso a arquivos em Python.

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
def verificarArquivo(arquivo):
    try:
        o = open(arquivo, 'rt')
        o.close()
    except FileNotFoundError:
        return False
    else:

        return True

def criarArquivo(arquivo):
    try:
        o = open(arquivo, 'wt+')
        o.close()
    except FileNotFoundError:
        return False
    else:
        print('Arquivo criado com sucesso!')

def lerArquivo(arquivo):
    try:
        o = open(arquivo, 'rt')

    except FileNotFoundError:
        print('Arquivo Não disponivel')
    else:
        for linha in o:
            linha = linha.rstrip().split(';')

            print(f'Nome: {linha[0]:<15}  {linha[1]:>20} anos')
    finally:
        o.close()


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
    print(f'{c["verde"]}{"OPÇÃO 1":^50}{c["limpa"]}')
    print('-' * 50)
    print(f'{c["azul"]}{"Lista de Pessoas":^50}{c["limpa"]}')

def opcao2():
    print('-' * 50)
    print(f'{c["verde"]}{"OPÇÃO 2":^50}{c["limpa"]}')
    print('-' * 50)
    print(f'{c["verde"]}{"Cadastre uma Pessoa":^50}{c["limpa"]}')

def opcao3():
    print('-' * 50)
    print(f'{c["vermelho"]}{"SAINDO DO SISTEMA":^50}{c["limpa"]}')

def menu():
    print('-' * 50)
    print(f'{c["magenta"]}{"MENU PRINCIPAL":^50} {c["limpa"]}')
    print('-' * 50)

    print(f'1 -{c["azul"]} Para ver pessoas cadastradas{c["limpa"]}')
    print(f'2 -{c["azul"]} Cadastrar novas pessoas{c["limpa"]}')
    print(f'3 -{c["azul"]} Sair do sistema{c["limpa"]}')
    print(f'-' * 50)

def cadastrar(arquivo, nome = 'desconhecido', idade = 0):
    try:
        o = open(arquivo, 'at')
    except:
        print('Houve um erro ao cadastrar no arquivo!')
    else:
        o.write(f'{nome}; {idade}\n')
        print('Cadastro feito com sucesso!')
    finally:
        o.close()



arquivo =  'Exercicio_0115.txt'
if not verificarArquivo(arquivo):
    criarArquivo(arquivo)

while True:
    menu()
    opcao = leiaInt('Digite a sua opção:')

    if opcao == 1:
        opcao1()
        lerArquivo(arquivo)

    elif opcao == 2:
        opcao2()
        nome = input('Digite seu nome: ')
        idade = leiaInt('Digite a sua idade: ')
        cadastrar(arquivo, nome, idade)

    elif opcao == 3:
        opcao3()
        break

    else:
        print(f'{c["vermelho"]}Digite um numero entre as OPÇÕES:{c["limpa"]}')



