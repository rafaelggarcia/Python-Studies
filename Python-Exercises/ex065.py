continuar = 'S'
quant = media = soman = 0
while continuar == 'S':
    n = int(input('Digite um número inteiro: '))
    quant += 1
    soman += n
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Você deseja continuar? [S/N]: ')).upper().strip()
media = soman / quant
print(f'Você digitou {quant} números e a média foi de {media}')
print(f'O maior valor digitado por você foi {maior} e o menor foi {menor}')
