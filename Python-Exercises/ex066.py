quant = soma = 0
while True:
    n = int(input(('Digite um número inteiro: ')))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'Você digitou {quant} números e a soma de todos eles é {soma}!')
