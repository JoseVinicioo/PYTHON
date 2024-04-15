p = 'S'
cont = cont2 = cont3 = 0
print('~'*18)
print('COLETADOR DE DADOS')
print('~'*18)
while p == 'S':
    i = int(input('Qual a idade? '))
    if i > 18:
        cont += 1
    s = ' '
    while s not in 'FM':
        s = str(input('E o sexo? [F/M] ')).upper().strip()[0]
    print('=-='*8)
    if s == 'M':
        cont2 += 1
    if s == 'F' and i < 20:
        cont3 += 1
    p = ' '
    while p not in 'SN':
        p = str(input(' Quer continuar? [S/N] ')).upper().strip()[0]
    print('=-='*8)
    if p == 'N':
        print('FIM DO PROGRAMA')
        print('=-=' * 8)
        break
print(f'{cont} pessoas tem mais que 18 anos.')
print(f'Foram cadastrados {cont2} homens.')
print(f'E {cont3} mulheres tem menos que 20 anos.')
