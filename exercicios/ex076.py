lista = ('Pão', 1, 'Leite', 3.5, 'Queijo', 5, 'Preseunto', 4, 'Frango', 25)
for list in range(0, len(lista), 2):
    print(f'{lista[list]:.<30}',end='')
    print(f'R${lista[list-1]:>7.2f}')






