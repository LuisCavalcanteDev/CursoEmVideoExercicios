#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tupla =  ('Arroz', 10, 'Feijão', 5, 'Macarrã', 6, 'Tomate', 8, 'Alface', 3, 'Carne', 20, 'Pepino', 3, 'Laranja', 5, 'Açucar', 4, 'Sal', 1 )


print(f'*' * 40)
print(f'{"LISTA DE PRODUTOS":^40}')
print(f'*' * 40)

for item in tupla:
    if type(item) is str:
        print(f'{item:.<30}', end = ' ')
    else:
        print(f'R$: {item:>5.2f}')

print(f'*' * 40)