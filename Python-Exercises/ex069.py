maiores = homens = mulheresmenores = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar cadastrando? [S/N]: ')).strip().upper()
    if idade >= 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheresmenores += 1
    if continuar == 'N':
        break
print(f'Foram cadastradas {maiores} pessoas maiores que 18 anos, {homens} homens e {mulheresmenores} mulheres menores que 20 anos!')
