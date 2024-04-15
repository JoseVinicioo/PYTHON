from random import randint
from time import sleep
from operator import itemgetter

rank = dict()
cont = 0

for j in range(1 , 5):
    rank[f'Jogador{j}'] = randint(1,6)
    rank.copy()
print("Valores Sorteados: ")
for k,v in rank.items():
    sleep(0.8)
    print(f'    O {k} tirou {v}')
print('Ranking dos Jogadores: ')
rank_ordem = list()
rank_ordem = sorted(rank.items(), key= itemgetter(1), reverse=True)
for i,v in enumerate(rank_ordem):
    sleep(0.76)
    print(f'    {i+1}° lugar: {v[0]} com {v[1]}')