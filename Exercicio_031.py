#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distância da sua viagem em km: '))

if distancia <= 200:
    valor = distancia * 0.50
    print(f'O valor da sua viagem foi R${valor:.2f}')
else:
    valor2 = distancia * 0.45
    print(f'O valor da sua viagem foi R${valor2:.2f}')
