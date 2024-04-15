from random import randint
cont = ma = me = 0
tupla = (randint(1,11),randint(1,11),randint(1,11),randint(1,11),randint(1,11))
print(f'Os números aleatorios gerados foram: ',end='')
for lista in tupla:
    print(lista, end=' ')
print(f'\nMAIOR NUM: {max(tupla)}\nMENOR NUM: {min(tupla)}')
