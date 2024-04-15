count = soma = n = 0
while n != 999:
    n = int(input('Digite um valor(999 para parar): '))
    count += 1
    soma += n
print('Foram lido {} números, e a soma entre eles foi de: {}'.format(count-1, soma - 999))