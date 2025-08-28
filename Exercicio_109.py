#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


import Exercicio_109_moeda

dinheiro = float(input('Digite um valor: '))
print(f'O valor {Exercicio_0109_moeda.moeda(dinheiro)} com aumento de 10% é: {Exercicio_0109_moeda.aumentar(dinheiro, True)}')
print(f'o valor {Exercicio_0109_moeda.moeda(dinheiro)} com desconto de 10% é: {Exercicio_0109_moeda.diminuir(dinheiro,True)}')
print(f'O dobro de {Exercicio_0109_moeda.moeda(dinheiro)} é: {Exercicio_0109_moeda.dobro(dinheiro,True)}')
print(f'A metade do valor {Exercicio_0109_moeda.moeda(dinheiro)} é: {Exercicio_0109_moeda.metade(dinheiro,True)}')







