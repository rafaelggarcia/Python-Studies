nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Você teve uma média de {media}, infelizmente foi reprovado.')
elif media > 5.0 and media < 6.9:
    print(f'Sua teve uma média de {media}, você está de recuperação.')
else:
    print(f'Você teve uma média de {media}, você foi aprovado!')
    