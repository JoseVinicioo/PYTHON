frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inverso = ''
for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]
print('O inverso de {}, é {}'.format(juntar,inverso))
if inverso == juntar:
    print('A frase é um palíndromo')
else:
    print('Não é um palíndromo')