totgasto = quantp = menor = cont = 0
barato = ' '
while True:
    nomeprod = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))
    cont += 1
    totgasto += preço
    if preço > 1000:
        quantp += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nomeprod
    continuar = ' '
    while not continuar in 'SN':
        continuar = str(input('Você deseja continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break
print(f'O total gasto foi {totgasto} e tiveram {quantp} produtos mais caros que 1000$ e o preço do produto mais barato foi {barato}.')
