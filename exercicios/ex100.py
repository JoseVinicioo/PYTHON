from random import randint
from time import sleep

numbers = list()
def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for sort in range(0,5):
        num = randint(0,10)
        numbers.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.5)  
    print('PRONTO!')
def somapar(lst):
    s = 0
    for values in range(0,5):
        if numbers[values]%2 == 0:
            s+=numbers[values]
    print(f'Somando os valores pares de {numbers}, temos {s}')

somapar(sorteia())