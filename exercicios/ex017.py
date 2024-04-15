from math import sqrt , pow
o = float(input('Digite o valor do cateto oposto: '))
a = float(input('Digite o valor do cateto adjacente: '))
h = sqrt(pow(a,2)+pow(o,2))
print('O comprimento da hipotenusa é: {}' .format(h))

from math import hypot
o = float(input('Digite o valor do cateto oposto: '))
a = float(input('Digite o valor do cateto adjacente: '))
h = hypot(o,a)
print('O comprimento da hipotenusa é: {}' .format(h))