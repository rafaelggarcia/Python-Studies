from random import  randint
computador = randint(0, 10)
acerto = False
palpites = 0
while not acerto:
    jogador = int(input('Qual o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acerto = True
    else:
        if jogador < computador:
            print('É maior, tente mais uma vez!')
        elif jogador > computador:
            print('É menor, tente mais uima vez!')
print(f'Você acertou com {palpites} palpites! Parabéns!')