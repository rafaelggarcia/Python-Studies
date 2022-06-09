from datetime import datetime
cadastro = {}
nome = str(input('Digite o nome: '))
nasc = int(input('Ano de nascimento: '))
idade = datetime.now().year - nasc
ctps = int(input('CTPS: '))
cadastro = {'Nome': nome, 'Idade': idade, 'CTPS': ctps}
if ctps != 0:
    cadastro['Contrato'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
aposentar = 35 - (datetime.now().year - cadastro['Contrato'])
print(f'Você irá se aposentar com {idade + aposentar} anos!')