import math
an = float(input('Digite o angulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print(' Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}' .format(sen,cos,tan))