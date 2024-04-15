print('$ '*8)
print('  LOJA DO ZÉ')
print('$ '*8)
bar = ''
cont = cont2 = som = me = 0
while True:
    print('-'*24)
    n = str(input('Nome do produto: '))
    p = float(input('Valor do produto: '))
    if p > 1000:
        cont += 1
    som += p
    cont2 += 1
    if cont2 == 1 or p < me:
        me = p
        bar = n
    print('-'*24)
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if c == 'N':
        break
print(f'O valor final da compra foi de: {som}R$')
print(f'{cont} produtos custam mais que \033[1;32mR$1.000,00\033[m')
print(f'O produto mais barato foi {bar} com o valor de {me}')
print('FIM DO PROGRAMA')
