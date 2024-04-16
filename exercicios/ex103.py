def ficha(jog=None, gols=0):
    if jog is None or jog.strip() == "":
        jog = "<desconhecido>"
    print(f'O jogador {jog} fez {gols} gols(s) no campeonato.')

print('-'*25)
n = input('Nome: ')
g = int(input('Gols: '))
ficha(n,g)