lista = []
for c in range( 0, 4 ):
    n = int( input( 'Digite um valor: ' ) )
    if c == 0:
        lista.append( n )
        print( 'Adicionado ao final da lista' )
    elif n > lista[len( lista ) - 1]:
        lista.append( n )
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert( pos, n )
                print( f'Adicionado na posição {pos}' )
                break
            pos += 1
print( f'Os valores digitados foram {lista}' )
lista = []