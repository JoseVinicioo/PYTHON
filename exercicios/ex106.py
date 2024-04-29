from time import sleep

def linhas(texto,cor):
    cont = len(texto)+4
    print('~'*cont)
    print(f'  {cor}{texto}\033[m')
    print('~'*cont)
def manual(prompt):
    sleep(0.5)
    linhas(f'Acessano o manual do comando "{parada}"','\033[46m')
    sleep(1.3)
    print('\033[30;47m')
    help(prompt)
    print('\033[m')
    sleep(2)

parada = ' '
while True:
    linhas('SISTEMA DE AJUDA PyHELP','\033[44m')
    parada = input('Função ou Biblioteca > ')
    if parada.upper() in 'FIM':
        linhas('ATÉ LOGO', '\033[41m')
        break
    else:
        manual(parada)
    
