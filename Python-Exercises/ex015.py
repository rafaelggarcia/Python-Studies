dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos quilometros foram rodados? '))

valor = (dias * 60) + (km * 0.15)

print(f'O valor a pagar pelo aluguel é {valor:.2f}')