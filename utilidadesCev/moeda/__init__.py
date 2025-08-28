#Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.


def aumentar(n, formatar=False):
     aumento =  n * 1.1
     return aumento if formatar is False else moeda(aumento)



def diminuir(n, formatar=False):
    desconto = n * 0.9
    return desconto if formatar is False else moeda(desconto)



def dobro(n, formatar=False):
    dobrado = n * 2
    return dobrado if formatar is False else moeda(dobrado)



def metade(n,formatar=False):
    meia = n / 2
    return meia if formatar is False else moeda(meia)

#Adapte o código do exercicio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
#Parte do exercicio 108

def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')



def resumo(valor):
    print('-' * 50)
    print(f'{"RESUMO DO VALOR":^50}')
    print('-' * 50)
    print(f'{"O valor analisado é":<25}{moeda(valor):>25}')
    print(f'{"10% de aumento:":<25}{aumentar(valor,True):>25}')
    print(f'{"10% de desconto:":<25}{diminuir(valor, True):>25}')
    print(f'{"Dobro do valor:":<25}{dobro(valor, True):>25}')
    print(f'{"Metade do valor:":<25}{metade(valor, True):>25}')
    print('-' * 50)



