import random
from time import sleep
import emoji
print('~-~'*8)
print(' JOGO DA ADVINHAÇÃO 2.0')
print('~-~'*8)
sleep(1.2)
cont = 1
comp = random.randint(1, 10)
print(emoji.emojize('\033[1;107;40m:rosto_de_robô: Pensei em um número entre 1 e 10\033[m', language='pt'))
sleep(0.6)
p = int(input('Qual seu palpite? '))
print(emoji.emojize('\033[7;107;40m:silhueta_falando:: {}\033[m'.format(p), language='pt'))
if 0 < p < 10:
    while p != comp:
        cont += 1
        if p > comp:
            print('Quase... um pouco MENOS!!!')
            p = int(input('Qual seu palpite? '))
            print(emoji.emojize('\033[7;107;40m:silhueta_falando:: {}\033[m'.format(p), language='pt'))
        if p < comp:
            print('Quase... um pouco MAIS!!!')
            p = int(input('Qual seu palpite? '))
            print(emoji.emojize('\033[7;107;40m:silhueta_falando:: {}\033[m'.format(p), language='pt'))
        if p == comp:
            print(emoji.emojize('\033[1;97;42mVOCÊ VENCEU!!!\033[m\n:rosto_de_robô: Foram necessaria {} tentativas'.format(cont+1), language='pt'))
else:
    print('Digite um valor entre 1 e 10!!')