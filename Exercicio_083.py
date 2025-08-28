#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. O seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = []
expressao = str(input('Digite uma frase: ')).upper().strip().split()
expressao_cortada = ''.join(expressao)

for valor in expressao_cortada:
    lista.append(valor)

if lista.count('(') == lista.count(')'):
    print('Está expressão está correta')
else:
    print('Esta expressão está errada')


