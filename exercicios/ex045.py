import random
from time import sleep
print('-_-'*6)
print('     \033[1;41;97mJOKENPÔ\033[m')
print('-_-'*6)
n = str(input('Pedra, Papel ou Tesoura?')).upper()
print('\033[1;31mJO...\033[m')
sleep(0.5)
print('\033[1;31mKEN...\033[m')
sleep(0.5)
print('\033[1;31mPÔÔ...\033[m')
sleep(0.8)
r = ['PEDRA','PAPEL','TESOURA']
r1 = random.choice(r)
if r1 == 'PEDRA' and n == 'TESOURA':
    print('A MAQUINA ESCOLHEU: PEDRAAA')
    sleep(2)
    print('\033[1;31mA maquina venceuu!!\033[m')
elif r1 == 'PEDRA' and n == 'PEDRA':
    print('A MAQUINA ESCOLHEU: PEDRAAA')
    sleep(2)
    print('\033[1;36mHouve um empate!!\033[m')
elif r1 == 'PEDRA' and n == 'PAPEL':
    print('A MAQUINA ESCOLHEU: PEDRAAA')
    sleep(2)
    print('\033[1;32mVocê vendeuu!!\033[m')
elif r1 == 'PAPEL' and n == 'PEDRA':
    print('A MAQUINA ESCOLHEU: PAPELLL')
    sleep(2)
    print('\033[1;31mA máquina venceu!!\033[m')
elif r1 == 'PAPEL' and n == 'PAPEL':
    print('A MAQUINA ESCOLHEU: PAPELLL')
    sleep(2)
    print('\033[1;36mHouve um empate!!\033[m')
elif r1 == 'PAPEL' and n == 'TESOURA':
    print('A MAQUINA ESCOLHEU: PAPELLL')
    sleep(2)
    print('\033[1;32mVocê venceuu!!\033[m')
elif r1 == 'TESOURA' and n == 'PEDRA':
    print('A MAQUINA ESCOLHEU: TESOURAAA')
    sleep(2)
    print('\033[1;32mVocê venceuu!!\033[m')
elif r1 == 'TESOURA' and n == 'PAPEL':
    print('A MAQUINA ESCOLHEU: TESOURAAA')
    sleep(2)
    print('\033[1;31mA máquina venceu!!\033[m')
elif r1 == 'TESOURA' and n == 'TESOURA':
    print('A MAQUINA ESCOLHEU: TESOURAAA')
    sleep(2)
    print('\033[1;36mHouve um empate!!\033[m')