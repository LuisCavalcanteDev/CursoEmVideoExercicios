#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumentar(n):
     aumento =  n * 1.1
     return aumento



def diminuir(n):
    desconto = n * 0.9
    return desconto



def dobro(n):
    dobrado = n * 2
    return dobrado



def metade(n):
    meia = n / 2
    return meia

#Adapte o código do exercicio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
#Parte do exercicio 108

def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')
