#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*notas, sit=False):
    dicionario = {}
    total = maior = menor = media = soma = 0


    for index,nota in enumerate(notas):

        if index == 0:
            maior = nota
            menor = nota
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota

        soma += nota
        total += 1


    dicionario['total'] = total
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = soma / total

    if sit:
        if dicionario['media'] >= 7:
            dicionario['situação'] = 'Boa'

        elif 5 <= dicionario['media'] < 7 :
            dicionario['situação'] = 'Regular'
        else:
            dicionario['situação'] = 'Pessima'

    return dicionario

resp = notas(4, 4, 5,9,8,7)
print(resp)