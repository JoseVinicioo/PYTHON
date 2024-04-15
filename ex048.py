s = 0
cont = 0
for c in range(0 , 500 , 3):
    if c % 2 == 1:
        s += c
        cont += 1
print('A SOMA ENTRE OS {} NUMEROS SOLICITADOS, ENTRE 1 ATE 500: {} '.format(cont,s))
