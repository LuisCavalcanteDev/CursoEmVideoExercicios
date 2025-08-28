#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input('Digite um número inteiro:'))

print('****TABUADA****')
for contador in range(1,11):
    print(f'{numero} * {contador}  = {numero * contador}')
print('FIM DA TABUADA')