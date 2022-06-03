n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opçao = 0
while opçao != 5:
    print('''Escolha uma das opções a seguir:
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Encerrar programa
        ''')
    opçao = int(input('Qual sua opção?'))
    if opçao == 1:
        print(f'A soma dos números {n1} e {n2} é {n1 + n2}')
    elif opçao == 2:
        print(f'A multiplicação dos números é {n1} e {n2} é {n1 * n2}')
    elif opçao == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}')
        elif n2 > n1:
            print(f'O maior número entre {n1} e {n2} é {n2}')
        else:
            print('Ambos são iguais!')
    elif opçao == 4:
        n1 = int( input( 'Digite o primeiro valor: ' ) )
        n2 = int( input( 'Digite o segundo valor: ' ) )
print('Você encerrou o programa!')

