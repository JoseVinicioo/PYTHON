n = float(input('Qual a distância da viajem em Km/h? '))
if n <= 200:
    v = n*0.50
else:
    v = n*0.45
print('O valor da passagem sera: {}R$'.format(v))