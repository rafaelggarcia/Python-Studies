lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um número para posição {c}: ')))
a = max(lista)
b = min(lista)
print(f'O maior valor digitado foi {a} e o menor valor digitado foi {b}')
print(f'O maior valor está na posição {lista.index(a)}')
print(f'O menor valor está na posição {lista.index(b)}')