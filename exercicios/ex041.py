from datetime import date
print('VEJA QUAL CATEGORIA DE NADADOR VOCÊ É')
d = int(input('Em qual ano você nasceu? '))
idade = date.today().year - d
print('Você tem {} anos'.format(idade))
if idade < 9:
    print('Faz parte da categoria: MIRIM')
elif idade <= 14:
    print('Faz parte da categoria: INFATIL')
elif idade <= 19:
    print('Faz parte da categoria: JUNIOR')
elif  idade <= 20:
    print('Faz parte da categoria: SÊNIOR')
else:
   print('Faz parte da categoria: MASTER')