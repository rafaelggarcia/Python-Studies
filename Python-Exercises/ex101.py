from datetime import date


def voto(ano=2001):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não Vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional'
    else:
        return f'Com {idade} anos: Voto obrigatório'


anonasc = int(input('Qual o ano em que você nasceu? '))
print(voto(anonasc))

