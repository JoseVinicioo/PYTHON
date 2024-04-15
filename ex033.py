n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro: '))
n3 = int(input('Digite outro: '))
m = n1
if n2<n1 and n2<n3:
    m=n2
if n3<n1 and n3<n2:
    m=n3
ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
     ma = n3
print('NÚMEROS: {},{},{}\nMENOR: {}\nMAIOR: {}'.format(n1,n2,n3,m,ma))