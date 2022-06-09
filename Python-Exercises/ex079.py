lista = []
while True:
    n = (int(input('Digite um número: ')))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado.')
    continuar = str(input('Você deseja continuar? ')).upper()
    if continuar == "N":
        break
lista.sort()
print(f'Os valores digitados foram {lista}')