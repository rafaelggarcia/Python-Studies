for x in range (1, 7):
    print(x)
print('Fim')

#ignora a ultima contagem, ou seja, para contar de 1 a 6, devo colocar de 1 a 7.

for z in range (7, 0, -1): #ou 2 para contar de 2 em 2
    print(z)
print('Fim')
# a ultima linha é o padrão de contagem.


i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for j in range (i, f+1, p):
    print(j)
print('Fim')

for k in range(0, 3):
    n = int(input('Digite um número: '))
print('Fim')