lista = []
for l in range(0, 5):
    n = (int(input('Digite um numero: ')))
    if l == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Número {n} adicionado no final')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista!!')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
