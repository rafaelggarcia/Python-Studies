preço = float(input('Digite o preço do produto: '))
print('''Escolha qual a sua opçao de pagamento:
        [1] À vista no dinheiro (10% de desconto).
        [2] À vista no cartão (5% de desconto). 
        [3] em até 2x no cartão (sem juros).
        [4] 3 ou mais vezes no cartão (20% de juros). 
''')
pagamento = int(input('Escolha sua forma de pagamento: '))

if pagamento == 1:
    novopreço = preço - (preço * 0.10)
    print(f'Você pagando à vista obteve 10% de desconto, o valor foi de {preço:.2f} R$ para {novopreço:.2f} R$ ')
elif pagamento == 2:
    novopreço = preço - (preço * 0.05)
    print(f'Você pagando a vista no cartão obteve 5% de desconto, o valor foi de {preço:.2f} R$ para {novopreço:.2f} R$')
elif pagamento == 3:
    print(f'Com o método de pagamento escolhido você não obteve desconto, o preço segue {preço:.2f} R$')
elif pagamento == 4:
    novopreço = preço + (preço * 0.20)
    print(f'Você parcelando em 3x ou mais como escolhido, o produto passa a custar {novopreço:.2f}R$')
else:
    print('Escolha uma forma de pagamento valida, apenas de 1 à 4.')
