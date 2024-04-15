from time import sleep
print('-_-' *10)
print('BEM VINDO AO CONVERSOR NUMERICO')
print('-_-' *10)
n = int(input('Digite um número: '))
v = str(input('CONVERTER PARA:\n1 - BINÁRIO\n2 - OCTAL\n3 - HEXADECIMAL\n'))
sleep(1)
if v == '1':
    print('Em binario: {}'.format(bin(n)[2:]))
elif v == '2':
    print('Em Octal: {}'.format(oct(n)[2:]))
elif v == '3':
    print('Em Hexadecimal: {}'.format(hex(n)[2:]))
else:
    print('Opção invalida, tente novamente!!')