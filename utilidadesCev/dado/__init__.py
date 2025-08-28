
def leiaDinheiro(msg):
    while True:
        entrada = input(msg).strip().replace(',', '.')
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print(f'\033[31mERRO: "{entrada}" não é um valor válido.\033[m')