while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        break
    for c in range(1, 11):
        m = c*n
        print(f'{c} x {n} = {m}')
print('FIM DO PROGRAMA!!Volte sempre :)')