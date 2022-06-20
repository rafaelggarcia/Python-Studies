from modulo109 import moeda

valor = int(input('Digite o valor que deseja aumentar? '))

print(f'O preço {moeda.moeda(valor)} aumentado em 10% é {moeda.aumentar(valor, True)}')
print(f'O preço {moeda.moeda(valor)} com desconto de 10% é {moeda.diminuir(valor, True)}')
print(f'O preço {moeda.moeda(valor)} dobrado é {moeda.dobro(valor, True)}')
print(f'O preço {moeda.moeda(valor)} pela metade é {moeda.metade(valor, True)}')
