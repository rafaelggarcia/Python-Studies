def escreva(texto):
    print(f'{"-" * len(texto)}')
    print(texto)
    print( f'{"-" * len(texto)}' )


texto = str(input('Digite o texto: '))
escreva(texto)