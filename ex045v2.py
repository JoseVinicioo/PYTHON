from random import randint
from time import sleep
import emoji
print('-_-'*6)
print('     JOKENPÔ')
print('-_-'*6)
sleep(1.5)
i = ('PEDRA', 'PAPEL', 'TESOURA')
c = randint(0,2)
print("[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA")
j = int(input('Qual sua escolha? '))
sleep(1.5)
print('-_-'*10)
print('Você jogou: \033[1;31m{}\033[m'.format(i[j]))
print('Computador jogou: \033[1;32m{}\033[m'.format(i[c]))
print('-_-'*10)
sleep(1)
if c == 0: #COMP JOGOU PEDRA
    if j == 0:
        print('Houve um empate')
    if j == 1:
        print('Você venceu')
    if j == 2:
        print('Você perdeu')
elif c == 1: #COMP JOGOU PAPEL
    if j == 0:
        print('Você perdeu')
    if j == 1:
        print('Houve um empate')
    if j == 2:
        print('Você venceu')
elif c == 2: #COMP JOGOU TESOURA
    if j == 0:
        print('Você venceu')
    if j == 1:
        print('Você perdeu')
    if j == 2:
        print('Houve um empate')
