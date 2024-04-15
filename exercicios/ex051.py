n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dec = n1 + (10 - 1) * r
for c in range(n1, dec + r, r):
    print('{} '.format(c), end='=> ')
print('FIM')