pessoas = list()
temp = list()
ma = me = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        me = ma = temp[1]
    else:
        if temp[1] > ma:
            ma = temp[1]
        if temp[1] < me:
            me = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[:1]
    if cont == 'N': break
print(f'Foram castradas {len(pessoas)} pessoas.')
for p in pessoas:
    if p[1] == ma:
        print(f'{p[0]}, ', end='') 
print(f' foi o MAIOR peso com {ma}Kg')
for p in pessoas:
    if p[1] == me:
        print(f'{p[0]}, ', end='') 
print(f' foi o MENOR peso com {me}Kg')
