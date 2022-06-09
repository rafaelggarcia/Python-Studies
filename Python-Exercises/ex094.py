geral = []
cadastro = {}
while True:
    cadastro['nome'] = str(input('Digite o nome: '))
    cadastro['sexo'] = str(input('Digite o sexo: ')).upper()
    cadastro['idade'] = int(input('Digite a idade: '))
    geral.append(cadastro.copy())
    cadastro.clear()
    continuar = str( input( 'Quer continuar? [S/N]: ' ) ).upper()
    if continuar == 'N':
        break
print('_' * 30)
print(f'Foram cadastradas {len(geral)} pessoas.')
media = somaidade = 0
for c, x in enumerate(geral):
    somaidade += geral[c]['idade']
    media = somaidade / len(geral)
print(f'A média da idade das pessoas cadastradas é {media}!')
totm = 0
for c, x in enumerate(geral):
    if geral[c]['sexo'] == 'F':
        totm += 1
print(f'O total de mulheres foi {totm}! ')
for c, x in enumerate(geral):
    if geral[c]['idade'] > media:
        print('Lista das pessoas acima da média: ')
        print(geral[c])