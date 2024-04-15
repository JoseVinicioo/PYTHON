import random
from time import sleep
print('~-~'*8)
print(' JOGO DA ADVINHAÇÃO 2.0')
print('~-~'*8)
sleep(1.4)
cont = 1
p = int(input('Digite um número entre 1 e 10: '))
if p != 0:
    comp = random.randint(1, 10)
    while p != comp:
        cont += 1
        print('\033[1;31mVOCÊ ERROU\033[m')
        print('Seu numero: {}'.format(p))
        print('Da maquina: {}'.format(comp))
        p = int(input('Tente novamente: '))
        comp = random.randint(1, 10)
        if comp == p:
            print('\033[1;32mVOCÊ VENCEU!!\033[m')
            print('Seu numero: {}'.format(p))
            print('Da maquina: {}'.format(comp))
            print('Foram necessaria {} tentativas'.format(cont))

