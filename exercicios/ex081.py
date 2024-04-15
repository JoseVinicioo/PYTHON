lista = []
while True:
    n = lista.append(int(input('Digite um valor: ')))
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).upper().strip()[:1]
    if c == 'N':
        break
print('-_-'*15)
print(f'Foram digitados {len(lista)} números')
print('-_-'*15)
print(f'A lista em forma decrescente: {sorted(lista, reverse=True)}')
print('-_-'*15)
if 5 in lista:
    print('O valor 5 foi digitado, e está na posição: ', end='')
    for i, v in enumerate(sorted(lista, reverse=True)):
        if v == 5:
            print(f'{i+1}...',)
else:
    print('O valor 5 NÃO foi digitado!!!')
print('-_-'*15)
