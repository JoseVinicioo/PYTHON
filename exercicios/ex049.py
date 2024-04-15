print('=-='*4)
print('\033[7;35mTABUADA 2.0 \033[m')
print('=-='*4)
n = int(input('Digite um numero: '))
for c in range(1 , 11):
    print("{} x {} = {} ".format(n,c,n*c))