from datetime import date
anoatual = date.today().year
ano = int(input('Digite o seu ano de nascimento: '))
idade = anoatual - ano
if idade <= 16:
    diferenca = 18 - idade
    print(f'Você ainda irá se alistar, não chegou a hora, faltam {diferenca}!')
elif idade == 17 or 18:
    print(f'Está na hora de você se alista!')
else:
    print('Vocé já ultrapassou o tempo de alistamento, a iadde correta é 18 anos.')