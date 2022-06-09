total = []
pessoas = []
while True:
    pessoas.append(input('Qual seu nome? '))
    pessoas.append(float(input('Qual seu peso? ')))
    if len(total) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        elif pessoas[1] < menor:
            menor = pessoas[1]
    total.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print(f'Foram cadastradas {len(total)} pessoas!')
print(f'A pessoa mais pesada é {maior} e a mais leve é {menor}')
