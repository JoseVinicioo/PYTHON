ma = 0
me = 0
for p in range(1,6):
    peso = float(input('Qual o peso da {}° pessoa? '.format(p)))
    if p == 1:
        ma = peso
        me = peso
    else:
        if peso > ma:
            ma = peso
        if peso < me:
            me = peso
print('O MAIOR peso é de {}Kg'.format(ma))
print('O MENOR peso é de {}Kg'.format(me))
