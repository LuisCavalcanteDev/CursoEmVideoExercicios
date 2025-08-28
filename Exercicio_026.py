#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.


frase = str(input('Digite uma frase: ')).strip().upper()

quantidade_a = frase.count('A')

posicao_inicial_a = frase.find('A') + 1
posicao_final_a = frase.rfind('A') + 1



print(f'Quantidade de A na frase é: {quantidade_a}')
print(f'Posição inicial da letra A na frase : {posicao_inicial_a}')
print(f'Posição final da letra A na frase : {posicao_final_a}')
