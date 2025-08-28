#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
maior_idade = 0
nome_velho = ''
contando_mulheres = 0

for contador in range(1, 5):
    nome = str(input(f'Qual o nome da {contador}ª pessoa? ')).strip()
    idade = int(input(f'Digite a idade da {contador}º pessoa? : '))
    sexo = int(input('Digite 1 para masculino e 2 para feminino:'))
    print('-----------------------------------------------------')
    soma_idade += idade

    if contador == 1:
        maior_idade = idade
    else:
        if idade > maior_idade and sexo == 1:
            maior_idade = idade
            nome_velho = nome

    if idade < 20 and sexo == 2:
        contando_mulheres += 1


media = soma_idade / 4

print(f'A média de idade do grupo é {media} anos')
print(f'O homem mais velho é o {nome_velho} ')
print(f'A quantidade de mulheres com menos de 20 anos é  {contando_mulheres}')