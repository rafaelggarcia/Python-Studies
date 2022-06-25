def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print(f'Erro: "{entrada}" é um preço inválido!')
        else:
            valido = True
            return float(entrada)
