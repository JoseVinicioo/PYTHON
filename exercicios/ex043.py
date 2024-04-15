a = float(input('Qual sua altura?(m) '))
p = float(input('Qual seu peso?(Kg) '))
IMC = p/(a**2)
print('O IMC dessa pessoa é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('SEU STATUS:\n\033[1;31mAbaixo do peso')
elif IMC <= 25:
    print('SEU STATUS:\n\033[1;32mPeso ideal')
elif IMC <= 30:
    print('SEU STATUS:\n\033[1;31mSobrepeso')
elif IMC <= 40:
    print('SEU STATUS:\n\033[1;31mObesidade')
else:
    print('SEU STATUS:\n\033[1;31mObesidade mórbida')
