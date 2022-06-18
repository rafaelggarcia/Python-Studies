from random import  randint
numeros = []


def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Os números sorteados foram {numeros}')

def  somapar(numeros):
    par = 0
    for i in numeros:
        if i % 2 == 0:
            par += i
    print(f'A soma dos números pares é {par}')

sorteia(numeros)
somapar(numeros)


