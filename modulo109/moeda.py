def aumentar(preço = 0, format=False):
    """

    :param preço: recebe o valor do item
    :return: retorno o valor 10% maior
    """
    result = preço + (preço * 0.10)
    return result if format is False else moeda(result)


def diminuir(preço = 0, format=False):
    """

    :param preço: recebe o valor do item
    :return: retorna o valor com 10% a menos
    """
    result = preço - (preço * 0.10)
    return result if format is False else moeda(result)



def dobro(preço = 0, format=False):
    """

    :param preço: recebe o valor do item
    :return: retorna o valor dobrado
    """
    result = preço * 2
    return result if format is False else moeda(result)



def metade(preço= 0, format=False ):
    """

    :param preço: recebe o valor do item
    :return: retorna o preço pela metade
    """
    result =  preço / 2
    return result if format is False else moeda(result)



def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


