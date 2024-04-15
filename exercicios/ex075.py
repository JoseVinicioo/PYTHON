
tupla = (int(input('Digite um valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite so mais um valor: ')))
print(f'VOCÊ DIGITOU {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram: ', end='')
for par in tupla:
    if par % 2 == 0:
        print(par, end=', ')
