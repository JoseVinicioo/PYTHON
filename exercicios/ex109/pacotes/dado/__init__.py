def leiaDinheiro(prompt):
    ok = False
    valor = 0
    while True:
        n = str(input(prompt))
        if n.isnumeric() or ',' in n:
            valor = int(n)
            ok = True
        else:
            print(f'\033[1;31mERRO!! Valor {n} não aceito!!\033[m')
        if ok:
            break
    return valor
