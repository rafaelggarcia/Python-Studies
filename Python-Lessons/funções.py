def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma desses valores é {s}')


soma(2, 4)


def contador(*num):
    for v in num:
        print(f'Recebi os valores {num} e são ao todo {len(num)})')

contador(1, 5, 9)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

lista = [2, 7, 9]
dobra(lista)
print(lista)

def somas(* valores):
    s = 0
    for num in valores:
        s += num
        print(f'Somando os valores {valores} temos {s}')