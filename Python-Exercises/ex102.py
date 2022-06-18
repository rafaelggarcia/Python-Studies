def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: o número a ser calculado
    :param show: mostra ou não a conta que foi realizada.
    :return: retorno o valor fatorial do número
    """
    """
    :param n: 
    :param show: 
    :return: 
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end=' ')

        f *= c
        return f


print(fatorial(5))