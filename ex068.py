from random import randint
cont = 0
v = ''
while True:
    cont += 1
    comp = randint(1, 10)
    n = int(input('Diga um valor: '))
    e = ' '
    while e not in 'PI':
        e = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('')
    par = (n + comp) % 2 == 0
    imp = (n + comp) % 2 != 0
    print('=-='*10)
    print(f'Você jogou {n} e computador {comp}. \nTOTAL {n + comp} ({'\033[1;32mPAR\033[m' if par else '\033[1;34mIMPAR\033[m'})')
    print('=-=' * 10)
    print('')
    if e == 'P' and par or e == 'I' and imp:
        print('\033[1;36mVOCÊ VENCEU\033[m')
    else:
        print('\033[1;31mVOCÊ PERDEU\033[m')
        print(f'GAME OVER! Você venceu {cont-1} vezes.')
        break
    print('Vamos jogar novamente...\n')
