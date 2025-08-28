#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

palavra = input("Escreva alguma coisa: ")

print(type(palavra))
print("É um número?",palavra.isnumeric())
print("É uma string?",palavra.isalpha())
print("É um alphanumerico?",palavra.isalnum())
print("Está em maiuscula?",palavra.isupper())
print("Está em minuscula?",palavra.islower())
print("Está capitalizada?",palavra.istitle())