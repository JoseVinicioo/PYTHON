d = float(input('Quantos dias alugado? '))
k = float(input('Quantos Km rodados? '))
q = (d*60)+(k*0.15)
print('Por ter ficado com o carro por {} dias e ter percorrido {}KM com ele, você pagará: {}' .format(d,k,q))