num = list()
pares = []
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar [S/N]: '))
    if resposta in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 ==0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista completa é {num}!')
print(f'A lista de pares é {pares}!')
print(f'A lista de impares é {impares}!')