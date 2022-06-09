aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
print(f'Nome é igual a {aluno["Nome"]}')
print(f'Média é igual a {aluno["Média"]}')
if aluno['Média'] >= 6.0:
    print(f'O aluno {aluno["Nome"]} está aprovado!')
else:
    print(f'O aluno {aluno["Nome"]} está reprovado!')