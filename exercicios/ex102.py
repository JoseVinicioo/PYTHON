def fatorial(num=0,show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    print('-'*25)
    for c in range(num,0,-1):
        f*=c
        if show == True:
            print('{} '.format(c), end='')
            print('x ' if c > 1 else '= ', end='')
    return f
""" help(fatorial) """
print(fatorial(5))