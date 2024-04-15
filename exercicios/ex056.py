ma = 0
nma = ''
s = 0
mu = 0
for c in range(1,5):
    print('----{}ª PESSOA----'.format(c))
    n = str(input('NOME: ')).strip()
    i = float(input('IDADE: '))
    se = str(input('SEXO[M/F]: ')).upper()
    s += i
    m = s/c
    if c == 1 and se in 'M':
        ma = i
        nma = n
    if se in 'M' and i > ma:
        ma = i
        nma = n
    if se in 'F' and i < 20:
        mu += 1
print('A media entre a idade das pessoas é {}'.format(m))
print('A pessoa mais velha dessa liste é {}, com {} anos'.format(nma , ma))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mu))

