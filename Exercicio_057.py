#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe o seu sexo (F/M): ')).upper().strip()

while  sexo != 'F' and sexo != 'M':
    print('Sexo invalido')
    sexo = str(input('Informe o seu sexo novamente (F/M): ')).upper().strip()

print('Valor informado corretamente!')


