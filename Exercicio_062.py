#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos


primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 0
total = 0
termos = 10

while termos != 0:
    total += termos
    while contador < total:
        print(primeiro_termo, end=' ')
        primeiro_termo += razao
        contador += 1
    termos = int(input('\nQuantos termos você quer mostrar a mais?: '))
print('FIM DO PROGRAMA')



