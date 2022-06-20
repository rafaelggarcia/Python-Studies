from modulo107 import moeda

valor = int(input('Digite o valor que deseja aumentar? '))

print(f'O preço aumentado em 10% é {moeda.aumentar( valor ):.2f} R$' )
print(f'O preço com desconto de 10% é {moeda.diminuir( valor ):.2f} R$' )
print(f'O preço dobrado é {moeda.dobro( valor ):.2f} R$' )
print(f'O preço pela metade é {moeda.metade( valor ):.2f} R$' )
