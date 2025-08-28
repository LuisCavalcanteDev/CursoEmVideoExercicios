#Adapte o código do exercicio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.



import Exercicio_107_moeda

dinheiro = float(input('Digite um valor: '))
print(f'O valor {Exercicio_0107_moeda.moeda(dinheiro)} com aumento de 10% é: {Exercicio_0107_moeda.moeda(Exercicio_0107_moeda.aumentar(dinheiro))}')
print(f'o valor {Exercicio_0107_moeda.moeda(dinheiro)} com desconto de 10% é: {Exercicio_0107_moeda.moeda(Exercicio_0107_moeda.diminuir(dinheiro))}')
print(f'O dobro de {Exercicio_0107_moeda.moeda(dinheiro)} é: {Exercicio_0107_moeda.moeda(Exercicio_0107_moeda.dobro(dinheiro))}')
print(f'A metade do valor {Exercicio_0107_moeda.moeda(dinheiro)} é: {Exercicio_0107_moeda.moeda(Exercicio_0107_moeda.metade(dinheiro))}')







