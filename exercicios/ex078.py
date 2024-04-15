lista = []
cont = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    ma = max(lista)
    me = min(lista)
print(lista)
print(f'MAIOR valor {ma}, na posição',end='')
for i, v in enumerate(lista):
    if v == ma:
        print(f' {i}...',end='')
print(f'\nMENOR valor {me}, na posição',end='')
for i, v in enumerate(lista):
    if v == me:
        print(f' {i}...',end='')