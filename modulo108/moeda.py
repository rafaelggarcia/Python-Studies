def aumentar(preço = 0):
    """

    :param preço: recebe o valor do item
    :return: retorno o valor 10% maior
    """
    return preço + (preço * 0.10)


def diminuir(preço = 0):
    """

    :param preço: recebe o valor do item
    :return: retorna o valor com 10% a menos
    """
    return preço - (preço * 0.10)


def dobro(preço = 0):
    """

    :param preço: recebe o valor do item
    :return: retorna o valor dobrado
    """
    return preço * 2


def metade(preço = 0 ):
    """

    :param preço: recebe o valor do item
    :return: retorna o preço pela metade
    """
    return preço / 2


def moeda(preço = 0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
