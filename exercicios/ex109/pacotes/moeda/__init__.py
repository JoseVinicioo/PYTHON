
def form(n):
    number = f'{n:.2f}'
    return f'R${str(number).replace(".",",")}'

def metade(n,moeda=False):
    metade = n/2
    if moeda:
        metade = form(metade)
    return metade


def dobro(n,moeda=False):
    dobro = n*2
    if moeda:
        dobro = form(dobro)
    return dobro
    

def aumentar(n,porcent, moeda=False):
    aument = n * (porcent/100) + n
    if moeda:
        aument = form(aument)
    return aument

def diminuir(n,porcent, moeda=False):
    dimin = n - n * (porcent/100)
    if moeda:
        dimin = form(dimin)
    return dimin

def resumo(n, aument, dimin):
    print('-'*20)
    print('  RESUMO DO VALOR')
    print('-'*20)
    print(f'Preço analisado:{form(n):>9}')
    print(f'Dobro dos preços:{dobro(n,True):>9}')
    print(f'Metade do preço:{metade(n,True):>10}')
    print(f'{aument}% de aumento:{aumentar(n,aument,True):>10}')
    print(f'{dimin}% de redução:{diminuir(n,dimin,True):>10}')