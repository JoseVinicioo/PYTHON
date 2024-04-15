soma = count = 0
c = 'S'
b = 0
ma = me = 0
while c == 'S':
    n = int(input('Digite um valor: '))
    c = str(input('Que continuar?[S/N] ')).upper().strip()[:1]
    count += 1
    soma += n
    if count == 1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
media = soma/count
print('A media entre os {} valores digitados foi: {:.2f}'.format(count,media))
print('Menor valor: {}\nMaior valor: {}'.format(me, ma))
