#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
         'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
         'PROGRAMADOR', 'FUTURO')

for item in tupla:
    print(f'Na palavra {item} temos: ', end='')
    for letra in item:
        if letra in 'AEIOU':
            print(f'{letra} ', end='')
    print('\n----------------------------------------')
