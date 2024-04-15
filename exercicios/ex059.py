from time import sleep
print('~-~'*8)
print(' ANÁLISADOR DE NÚMEROS')
print('~-~'*8)
n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
menu = 0
while menu < 5:
    soma = n1 + n2
    multi = n1 * n2
    sleep(1.3)
    print('')
    print('[ 1 ] SOMA\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA')
    menu = int(input('Escolha uma opção: '))
    if menu == 1:
        print('\033[1;36mA SOMA dos valores {} e {} é: {}\033[m'.format(n1, n2, soma))
    elif menu == 2:
        print('\033[1;32mA MULTIPLICAÇÃO dos valores {} e {} é: {}\033[m'.format(n1, n2, multi))
    elif menu == 3:
        if n1 > n2:
            print('\033[1;31mO maior valor é: {}\033[m'.format(n1))
        if n2 > n1:
            print('\033[1;31mO maior valor é: {}\033[m'.format(n2))
    elif menu == 4:
        n1 = float(input('Digite o 1° número: '))
        n2 = float(input('Digite o 2° número: '))
    print('-=-'*15)
print('VOCÊ SAIU DO ANALISADOR')

