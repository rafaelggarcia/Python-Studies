from random import randint
vitorias = 0
while True:
    escolha = str(input('Digite oque deseja [Impar/Par]: ')).upper().strip()
    pc = randint( 1, 10 )
    user = int(input('Digite um número para jogar: '))
    soma = pc + user
    if escolha == 'PAR' and soma % 2 == 0 or escolha == 'IMPAR' and soma % 2 != 0:
        print('Parabéns você venceu!')
        vitorias += 1
    else:
        break
print(f'Você perdeu, o computador escolheu {pc} e você {user}, porém você obteve {vitorias} vitórias seguidas!')



