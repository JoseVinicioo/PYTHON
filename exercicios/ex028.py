import random
from time import sleep
print('-=-'*15)
print('    Pensando em um numero entre 0 e 5...')
print('-=-'*15)
sleep(2)
r = random.randint(0, 5)
p = int(input('Qual foi o numero pensado pelo programa? '))
if p == r:
    print('PARABENS, o número pensado foi {}' .format(r))
else:
    print('VOCÊ ERROU, o numero pensado foi {}' .format(r))