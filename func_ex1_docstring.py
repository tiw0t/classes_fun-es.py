import pydoc
def quadrado(n):
    """Retorna o quadrado de um número."""
    return n ** 2

def somar(a, b=0):
    """
    argumentos:
    soma dois números e retorna o resultado.
    a (número): O primeiro número.
    b (número, opcional): O segundo número. padrão é 0.

    retorno:
        numerico:  A soma dos dois número.

    exemplos:

    >>> somar(5,3)
    8
    >>> somar (10)
    10
    """
    return a+b