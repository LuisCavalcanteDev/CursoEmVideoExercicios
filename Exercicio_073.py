lista_cores = {
    "preto": '\033[0;30m',
    "vermelho": '\033[0;31m',
    "verde": '\033[0;32m',
    "amarelo": '\033[0;33m',
    "azul": '\033[0;34m',
    "branco": '\033[0;37m'
}

times = (
    "Flamengo",
    "Cruzeiro",
    "Red Bull Bragantino",
    "Palmeiras",
    "Fluminense",
    "Botafogo",
    "Bahia",
    "Mirassol",
    "Atlético Mineiro",
    "Ceará",
    "Corinthians",
    "Grêmio",
    "São Paulo",
    "Internacional",
    "Vasco da Gama",
    "Vitória",
    "Fortaleza",
    "Santos",
    "Juventude",
    "Sport Recife"
)

print('=-*' * 30)
print(lista_cores["verde"] + f'Os 5 primeiros times são: \n{times[0:5]}' + '\033[0m')
print('=-*' * 30)
print(lista_cores["vermelho"] + f'Os 4 últimos colocados são: \n{times[-4:]}' + '\033[0m')
print('=-*' * 30)
print(lista_cores["amarelo"] + f'Times em ordem alfabética: \n{sorted(times)}' + '\033[0m')
print('=-*' * 30)
print(lista_cores["azul"] + f'O santos está em: {times.index("Santos") + 1}º lugar' + '\033[0m')
