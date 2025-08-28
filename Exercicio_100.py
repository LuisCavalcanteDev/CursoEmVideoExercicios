#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.


from random import randint
lista_sorteada = []

def sorteia():
    for _ in range(5):
        lista_sorteada.append(randint(1,10))



def somaPar(lista):
    somar = 0
    for i in lista:
        if i % 2 == 0:
            somar += i
    print(f'A soma dos valores é {somar}')



sorteia()

print(f'A lista sorteada foi: {lista_sorteada}')
somaPar(lista_sorteada)

