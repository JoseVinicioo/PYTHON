print('TESTADOR DE POLINDROMOS')
f = str(input('Digite uma frase: ')).replace(" ","").upper()
i = f[::-1]
print('O inverso de {}, é {}'.format(f,i))
if i == f:
    print('Esta frase é um POLINDROMO!!')
else:
    print('Esta  frase NÃO é um PALINDROMO!!')