from datetime import date
from time import sleep
n = int(input('Digite um ano para ser analisado ou 0 para analisar o ano atual:'))
print('ANALISANDO...')
sleep(2)
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('O ano {} é bissexto!!'.format(n))
else:
    print('O ano {} NÃO é bissexto!!'.format(n))