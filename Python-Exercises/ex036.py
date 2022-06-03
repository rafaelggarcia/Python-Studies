valorcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do salario? '))
anos = int(input('Em quantos anos a casa será paga? ')) * 12
valorprestaçao = valorcasa / anos
salario30 = salario * 0.30
if valorprestaçao > salario30:
    print(f'O seu financiamento foi negado! ')
else:
    print('Seu financiamento está aprovado! Parabéns pela aquisição!')