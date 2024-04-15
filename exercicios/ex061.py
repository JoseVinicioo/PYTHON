n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
termo = n1
while cont <= 10:
    print('{}'.format(termo), end=' => ')
    termo += r
    cont += 1
print('FIM')
