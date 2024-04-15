from random import randint
from time import sleep
palpites = list()
jogo = list()
print("-"*20)
print("\033[1m JOGA NA MEGA SENA\033[m")
print("-"*20)
qnt = int(input("Quantos jogos voce quer que eu sorteie? "))
for i in range(0,qnt):
    for l in range(0,6):
        num = randint(1,60)
        if num in jogo:
            num = randint(1,60)
        jogo.append(num)
    palpites.append(jogo[:])
    jogo.clear()
print(f"-=-=-= SORTEANDO {qnt} JOGOS -=-=-=")
for i in range(0,qnt):
    sleep(1.5)
    print(f"Jogo {i+1}: {sorted(palpites[i])}")