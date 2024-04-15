#SOMA APENAS DOS NUMEROS PARES
print('=-='*12)
print('CALCULADORA APENAS DE NUMEROS PARES')
print('=-='*12)
s = 0
for c in range(1,3):
    nums = int(input('Digite o {}° valor: '.format(c)))
    if nums % 2 == 0:
        s += nums
print('SOMA DOS PARES: {}'.format(s))