import random
from random import choice
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorteio = random.choice(number)
numberuser = int(input('Digite um número de 1 a 9: '))
if numberuser == sorteio:
    print(f'O computador também escolheu {number}, parabéns você venceu!')
else:
    print(f'O computador escolheu {sorteio}, você perdeu!')
    