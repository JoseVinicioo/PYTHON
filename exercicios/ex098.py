from time import sleep
def contador(inicio,fim,passo):
    if passo < 0:
        passo*= -1
    elif passo == 0:
        passo = 1
    print('-='*17)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)
    if inicio<fim:
        while inicio <= fim:
            print(f'{inicio} ', end='', flush=True)
            sleep(0.3)
            inicio+=passo
        print('FIM!!')
    else:
        while inicio >= fim:
            print(f'{inicio} ', end='', flush=True)
            sleep(0.3)
            inicio-=passo
        print('FIM!!')
    
contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
m = int(input('Meio: '))
f = int(input('Fim: '))
contador(i,m,f)
    