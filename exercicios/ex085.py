pares = []
impares = []
nuns = [[pares], [impares]] 

for i in range(0, 7):
    num = int(input(f"Digite o {i+1}º valor: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'Os valores PARES digitados foram: {sorted(pares)}')
print(f'Os valores ÍMPARES digitados foram: {sorted(impares)}')
