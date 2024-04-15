n = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes.' .format(n.count('A')))
print('A primeira letra A, esta na posição {}' .format(n.find('A') +1))
print('A ultima letra A, esta na posição {}' .format(n.rfind('A') +1))