from random import shuffle
name1 = str(input('Digite o número do primeiro aluno: '))
name2 = str(input('Digite o número do segundo aluno: '))
name3 = str(input('Digite o número do terceiro aluno: '))
name4 = str(input('Digite o número do qaurto aluno: '))

lista = [name1, name4, name3, name2]

shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)
