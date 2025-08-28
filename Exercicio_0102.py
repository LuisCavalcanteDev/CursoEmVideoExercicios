#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(numero, show=False):
    """
    Calcula o fatorial de um número.

    Parâmetros:
    numero -- número inteiro a ser calculado o fatorial
    show -- (opcional) se True, mostra o processo de multiplicação

    Retorna:
    O valor do fatorial
    """
    total = 1
    for i in range(numero, 0, -1):
        if show:
            print(i, end=' ')
            if i > 1:
                print('x', end=' ')
            else:
                print('= ', end='')
        total *= i

    return total


# Exemplo de uso:
print(fatorial(3, True))