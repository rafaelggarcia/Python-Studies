from datetime import date
ano = date.today().year
contmenor = 0
contmaior = 0
for c in range(0, 7):
    nascimento = int(input('Digite o ano de nascimento: '))
    if ano - nascimento < 18:
        contmenor += 1
    else:
        contmaior += 1
print(f'Das 7 pessoas {contmenor} não atingiram a maior idade e {contmaior} já são maiores!'
)
