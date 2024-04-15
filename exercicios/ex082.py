lista = list()
listpar = []
listim = []
while True:
    n = (int(input('Digite um valor: ')))
    if n % 2 == 0:
        listpar.append(n)
    else:
        listim.append(n)
    lista.append(n)
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar [S/N]: ')).upper().strip()[:1]
    if c == 'N':
        break
print('^ '*25)
print(f'Os números digitados foram {lista}')
print('^ '*25)
print(f'Os números PARES são {listpar}')
print('^ '*25)
print(f'Os números IMPARES são {listim}')
print('^ '*25)
