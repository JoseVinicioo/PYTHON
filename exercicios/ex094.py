todos = list()
pessoa = dict()
som = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in "FM":
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[:1]
    pessoa['idade'] = int(input('Idade: '))
    todos.append(pessoa.copy())
    pessoa.clear()
    cont = ' '
    while cont not in "SN":
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[:1]
    if cont == "N": break
print('-='*15)
print(f'- O grupo tem {len(todos)} pessoas.')
for pessoa in todos:
    if 'idade' in pessoa:
        som+=pessoa['idade']
print(f'- A média das idades é: {som/len(todos)} anos')
print('- As mulheres castradas foram:', end=' ')
for p in todos:
    if p['sexo'] == 'F':
        print(p['nome'], end=', ')
print('\n- Lista das pessoas que estão acima da média: ')
for pessoa in todos:
    if pessoa['idade'] > (som/len(todos)):
        print(' ', end='')
        for k,v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRANDO >>')


