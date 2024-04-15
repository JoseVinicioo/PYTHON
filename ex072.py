num = int(input('Digite um número entre 0 e 20: '))
nuns = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while num > 20 or num < 0:
    print('Tente novamente. ', end='')
    num = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número \033[1;34m{nuns[num]}\033[m!!')
