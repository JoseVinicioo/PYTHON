n = int(input('Digite um valor: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;33m', end=' ')
        tot += 1
    else:
        print('\033[1;31m', end=' ')
    print('{} '.format(c), end=' ')
if tot == 2:
    print('\nO NÚMERO {} FOI DIVISIVEL {} VEZES, E É PRIMO'.format(n,tot))
elif tot > 2:
    print('\nO NÚMERO {} FOI DIVISIVEL {} VEZES, E NÃO É PRIMO'.format(n,tot))