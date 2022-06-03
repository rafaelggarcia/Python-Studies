salario = float(input('Digite o valor do salário: '))

if salario > 1250:
    aumento10 = salario * 0.10
    salario += aumento10
    print(f'O seu aumento foi de 10%, seu salario atual é de {salario}')
else:
    aumento15 = salario * 0.15
    salario += aumento15
    print(f'O seu aumento foi de 15%, seu salario atual é de {salario}')

