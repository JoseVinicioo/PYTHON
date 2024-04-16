from time import sleep
import sys

def linhas(texto,cor):
    cont = len(texto)+4
    print('~'*cont)
    print(f'  {cor}{texto}\033[m')
    print('~'*cont)
def manual(prompt):
    parada = ' '
    while True:
        linhas('SISTEMA DE AJUDA PyHELP','\033[44m')
        sys.stdout.flush()
        parada = input(prompt).upper()
        if parada in 'FIM':
            linhas('ATÉ LOGO', '\033[41m')
            break
        sleep(0.5)
        linhas(f'Acessano o manual do comando "{parada}"','\033[46m')
        sys.stdout.flush()
        sleep(1.3)
        print('\033[30;47m')
        print(help(parada))
        print('\033[m')
        sys.stdout.flush()
        sleep(2)


n = manual('Função ou Biblioteca > ')