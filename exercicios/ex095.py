dados = dict()
gols = list()
jogs = list()
conta = 0
while True:
    dados['nome'] = str(input('Nome do jogador: '))
    qnt = int(input(f'Quantas partidadas {dados["nome"]} jogou? '))
    for c in range(0, qnt):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    jogs.append(dados.copy())
    gols.clear()
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[:1]
    if cont == 'N': break
    print('-'*40)
print('-='*25)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k,v in enumerate(jogs):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    n = int(input('Mostrar dados de qual jogador? (Digite 999 para sair) '))
    if n == 999:
        break
    if n >= len(jogs):
        print('Jogador não encontrado.')
        continue
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogs[n]["nome"]}: ')
        for i, g in enumerate(jogs[n]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
print('<< VOLTE SEMPRE >>')
