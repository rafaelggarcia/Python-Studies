num = int(input('Digite um número inteiro: '))
print('''Escolha sua base para conversão:
        [1] Binário
        [2] Octal
        [3] Hexadecimal''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'Convertemos o número {num} para binário, o valor é {bin(num)}')
elif opcao == 2:
    print(f'Convertemos o número {num} para octal, o valor é {oct(num)}')
else:
    print(f'Convertemos o número {num} para hexadecimal, o valor agora é {hex(num)}')

