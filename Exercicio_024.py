#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

cidade = str(input('Digite o nome da cidade:')).strip().upper()


primeiro_nome_cidade = cidade.split()[0]

comparacao = 'SANTO' in primeiro_nome_cidade

print(comparacao)

