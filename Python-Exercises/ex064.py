n = numerosdigitados = soma = 0
while n != 999:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n != 999:
        soma += n
        numerosdigitados += 1
print(f'Você digitou {numerosdigitados} números e a soma deles é {soma}!')

###ambos as maneiras de fazer o exercicio. 

n = numerosdigitados = soma = 0
n = int(input('Digite um número inteiro (999 para parar): '))
while n != 999:
    n = int(input('Digite um número inteiro (999 para parar): '))
    soma += n
    numerosdigitados += 1
print(f'Você digitou {numerosdigitados} números e a soma deles é {soma}!')