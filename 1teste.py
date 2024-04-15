import random
print('~'*11)
print('  TABUADA')
print('~'*11)
v = int(input('''Tabuada do numero: '''))
print('~'*18)
print('''[ 1 ] SOMA
[ 2 ] SUBTRAÇÃO
[ 3 ] MULTIPLICAÇÃO
[ 4 ] DIVISÃO
[ 5 ] SAIR DO PROGRAMA''')
print('~'*20)
n = int(input('Escolha uma opção: '))
print('~'*20)
while n > 5:
    print('Digite um valor válido')
    n = int(input('Escolha uma opção: '))
x = ''
if n == 5:
    print('SAINDO DO PROGRAMA')
elif n == 1:
    x = 'SOMA'
    s = '+'
    for c in range(1, 11):
        print('{} {} {} = {}'.format(v,s, c, v + c))
elif n == 2:
    sub = 0
    x = 'SUBTRAÇÃO'
    s = '-'
    for c in range(1, 11):
        if c - v <= 0:
            sub = v - c
        else:
            sub = c - v
        print('{} {} {} = {}'.format(v, s, c, sub))
elif n == 3:
    x = 'MULTIPLICAÇÃO'
    s = 'x'
    for c in range(1, 11):
        print('{} {} {} = {}'.format(v, s, c, v * c))
elif n == 4:
    x = 'DIVISÃO'
    s = ':'
    for c in range(1, 11):
        print('{} {} {} = {:.2f}'.format(v, s, c, v / c))
print('~'*20)


