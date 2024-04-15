from time import sleep
def maior(*num):
    ma = 0
    tot = len(num)
    for nuns in num:
        if num == 0:
            nuns = ma
        else:
            if nuns > ma:
                ma = nuns
    print('-='*25)
    print(f'Analisando os valores passados...')
    sleep(1.5)
    for c in num:
        print(f'{c} ', end='', flush=True)
        sleep(0.3)
    print(f'Foram informados {tot} valores ao todo.')
    print(f'O maior valor informado foi {ma}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1,2)
maior(6)
maior()