n = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em MAIÚSCULO: {}'.format(n.upper()))
print('Seu nome em MINÚSCULO: {}'.format(n.lower()))
print('Seu nome tem {} letras, sem incluir espaços.'.format(len(n)-n.count(' ')))
s = n.split()[0]
print('Seu primeiro nome é: {}, e tem {} letras.' .format(s , n.find(' ')))