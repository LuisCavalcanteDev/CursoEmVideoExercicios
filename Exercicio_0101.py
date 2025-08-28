#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.



def voto(data):
    from datetime import date
    atual = date.today().year

    idade = atual - data


    if 16 <= idade < 18 or idade > 65:
        print(f'O seu voto é OPCIONAL ')
    elif idade < 16:
        print(f'O seu voto é NEGADO ')
    else:
        print(f'O seu voto é OBRIGATÓRIO ')




ano = int(input('Digite o ano de nascimento: '))

voto(ano)