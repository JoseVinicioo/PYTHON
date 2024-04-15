lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        a = lista[:]
        a.remove(num)
        print('VALOR DUPLICADO!!\033[1;31m NÃO VOU ADICIONAR!!\033[m')
    else:
        lista.append(num)
        print('VALOR ADICIONADO COM SUCESSO...')
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar [S/N] ')).upper().strip()[:1]
    if c == 'N':
        break
print('=-='*18)
print(f'Você digitou os valores {sorted(lista)}')
