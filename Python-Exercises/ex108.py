from modulo108 import moeda

valor = int(input('Digite o valor que deseja aumentar? '))

print(f'O preço {moeda.moeda(valor)} aumentado em 10% é {moeda.moeda(moeda.aumentar( valor ))}')
print(f'O preço {moeda.moeda(valor)} com desconto de 10% é {moeda.moeda(moeda.diminuir( valor ))}')
print(f'O preço {moeda.moeda(valor)} dobrado é {moeda.moeda(moeda.dobro( valor ))}')
print(f'O preço {moeda.moeda(valor)} pela metade é {moeda.moeda(moeda.metade( valor ))}')
