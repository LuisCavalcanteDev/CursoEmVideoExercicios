#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior_que_18 = 0
homens = 0
mulheres_menor_20 = 0

while True:
    print('-=' * 30)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo: [F/M] ')).upper().strip()[0]
    print('-=' * 30)




    if idade >= 18:
        maior_que_18 += 1

    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1

    progressao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if progressao == 'N':
        break

print(f'Maiores de 18 anos: {maior_que_18}')
print(f'Quantidades de homens cadastrado foi {homens}')
print(f'Mulheres menor de 20 anos: {mulheres_menor_20}')