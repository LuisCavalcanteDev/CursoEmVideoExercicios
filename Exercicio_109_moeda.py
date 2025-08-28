#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.


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
