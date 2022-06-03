from random import choice
name1 = str(input('Digite o nome do primeiro aluno: '))
name2 = str(input('Digite o nome do segundo aluno: '))
name3 = str(input('Digite o nome do terceiro aluno: '))
name4 = str(input('Digite o nome do qaurto aluno: '))

lista = [name1, name4, name3, name2]

escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')