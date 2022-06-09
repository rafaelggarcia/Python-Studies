par = []
impar = []
ambos = []
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
ambos.append(par)
ambos.append(impar)
print(f'Os valores pares em ordem são {sorted(ambos[0])}')
print(f'Os valores impares em ordem são {sorted(ambos[1])}')