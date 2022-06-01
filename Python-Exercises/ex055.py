for c in range(0, 5):
    peso = float( input( 'Digite o peso: ' ) )
    if c == 0:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print(f'O maior peso é {pesomaior}, e o menor peso é {pesomenor}')
