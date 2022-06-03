n = int(input('Digite um número inteiro de 0 a 9999: '))
n = str(n)

print(f'Unidade: {n[0]}')
print(f'Dezena: {n[1]}')
print(f'Centena: {n[2]}')
print(f'Milhar: {n[3]}')

# na forma matematica

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10