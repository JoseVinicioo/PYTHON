cont = 0
n = int(input('Quanto o valor sacado? '))
tot = n
ced = 50
totce = 0
while True:
    if tot >= ced:
        tot -= ced
        totce += 1
    else:
        if totce > 0:
            print(f'Total de {totce} celulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totce = 0
        if tot ==0:
            break