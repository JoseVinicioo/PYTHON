def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato.')

n = str(input("Nome: "))
g = str(input("Gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n,g)