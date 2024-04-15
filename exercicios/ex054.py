from datetime import date
print('TESTE DE IDADE')
for c in range(1,8):
    a = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    i = date.today().year - a
    if i >= 18:
        print('Você tem {} anos, e é: MAIOR DE IDADE'.format(i))
    else:
        print('Você tem {} anos, e é: MENOR DE IDADE'.format(i))
