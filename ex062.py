n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
termo = n1
m = 10
total = 0
while m != 0:
    total = total + m
    while cont <= total:
        print('{}'.format(termo), end=' => ')
        termo += r
        cont += 1
    print('PAUSA')
    m = int(input('Quantos termos quer ver? '))
print(f'Foram mostrados {cont-1} termos')
