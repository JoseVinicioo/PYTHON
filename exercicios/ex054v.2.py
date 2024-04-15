from time import sleep
from datetime import date
print('TESTE DE IDADE')
cont = 0
for c in range(1,8):
    a = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    i = date.today().year - a
    if i >= 18:
        cont += 1
    else:
        ''
sleep(0.6)
print('{} pessoas são MAIORES de idade'.format(cont))
print('{} pessoas são MENORES de idade'.format(c - cont))
