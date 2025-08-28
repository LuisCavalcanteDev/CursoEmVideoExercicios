#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual a velocidade que você estava?'))

if velocidade <= 80:
    print('Você está na velocidade correta. \nTenha uma boa viajem.')
else:
    multa = (velocidade - 80) * 7
    print('Você está acima da velocidade...')
    print(f'Precisa pagar uma multa com o valor de R${multa}')
