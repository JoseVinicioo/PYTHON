r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
a = r1+r2 > r3 and r2+r3 > r1 and r3+r1 > r2
if a:
    print('Sim, é possivel formar um triangulo')
else:
    print('Não é possivel formar um triangulo')