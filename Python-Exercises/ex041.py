from datetime import date
idade  = date.today().year - int(input('Digite o ano de nascimento do atleta: '))
if idade <= 9:
    print('Você é um atleta MIRIM!')
elif idade <= 14:
    print('Você é um atleta INFANTIL!')
elif idade <= 19:
    print('Você é um atleta JUNIOR!')
elif idade == 20:
    print('Você é um atleta SÊNIOR!')
else:
    print('Você é um atleta MASTER!')

