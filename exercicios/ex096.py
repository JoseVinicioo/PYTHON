def area(c,l):
    a = c*l
    print(f'A área de um terreno {c}x{l} é de {a}m²')

print('  Controle de Terrenos')
print('-'*25)
c = float(input('Comprimento: '))
l = float(input('Largura: '))
area(c,l)