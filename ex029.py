from color50 import Color , constants
v = float(input('Qual sua velocidade em Km/h? '))
p = (v-80)*7
ver = Color()
ver.red = 255
if v >80:
    print('Calma ai parceiro, esta dirigindo muito rapido')
    print(ver + 'Terá que pagar uma multa de {}R$' .format(p) + constants.RESET )
else:
    print('Você esta na velocidade adequada')