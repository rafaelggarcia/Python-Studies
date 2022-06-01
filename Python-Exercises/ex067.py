while True:
    n = int(input('Digite um número para ver a sua tabuada: '))
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{c:2} x {n:2} = {c * n:2}')
print('Você encerrou o programa!')