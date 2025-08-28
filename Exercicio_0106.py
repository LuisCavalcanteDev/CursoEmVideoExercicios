#Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
cores = {
    'preto':     '\033[30m',
    'vermelho':  '\033[31m',
    'verde':     '\033[32m',
    'amarelo':   '\033[33m',
    'azul':      '\033[34m',
    'magenta':   '\033[35m',
    'ciano':     '\033[36m',
    'branco':    '\033[37m',

    'fundo_preto':    '\033[40m',
    'fundo_vermelho': '\033[41m',
    'fundo_verde':    '\033[42m',
    'fundo_amarelo':  '\033[43m',
    'fundo_azul':     '\033[44m',
    'fundo_magenta':  '\033[45m',
    'fundo_ciano':    '\033[46m',
    'fundo_branco':   '\033[47m',

}
r = '\033[0m'


def ajuda(comando):
    print(cores['fundo_ciano'], cores['preto'])
    help(comando)
    print(r)



comando = ''

while True:
    print(f'{cores['fundo_magenta']}{" SAIBA MAIS PYTHON ":*^80} {r}')
    print(cores['verde'])
    comando =  str(input('Digite um comando para informações: '))
    print(r)
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)


help(print)