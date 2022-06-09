lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Você deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é {lista}')
if 5 in lista:
    print(f'A lista tem o número 5 digitado!')
else:
    print(f'A lista não tem o número 5 digitado!')