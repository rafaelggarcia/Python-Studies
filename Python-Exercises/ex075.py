valores = tuple(int(input('Digite valores:  ')) for c in range(1, 5))
print(f'Você digitou os valores {valores}!')
print(f'O número 9 apareceu {valores.count(9)} vezes')
if 4 in valores:
    print(f'O número 4 apareceu na posição {valores.index(4)+1}')
else:
    print('O valor 4 não foi digitado em nenhum posição!')
print( f'Os números pares são ', end='' )
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
