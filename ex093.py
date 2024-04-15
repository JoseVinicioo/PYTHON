dados = dict()
gols = list()
dados['nome'] = str(input('Nome do jogador: '))
qnt = int(input(f'Quantas partidadas {dados["nome"]} jogou? '))
for c in range(0, qnt):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-='*20)
print(dados)
print('-='*20)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i,c in enumerate(dados['gols']):
    print(f'    => Na partida {i}, fez {c} gols.')
print(f'Foram um total de {dados["total"]} gols.')
