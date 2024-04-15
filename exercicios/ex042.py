l1 = float(input('Valor da 1° reta: '))
l2 = float(input('Valor da 2° reta: '))
l3 = float(input('Valor da 3° reta: '))
t = l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1
if t:
    print('Os seguimentos acima \033[1;32mPODEM FORMAR UM TRIANGULO: ', end='')
    if t and l1 == l2 == l3:
        print('EQUILATERO')
    elif t and l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima \033[1;31mNÃO PODEM FORMAR UM TRIANGULO\033[m')