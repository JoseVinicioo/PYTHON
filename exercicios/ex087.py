matriz = [[],[],[]]
soma = 0
for i in range(0,3):
    n0 = int(input(f"Digite o valor da posicao [0,{i}]: "))
    if n0 % 2 == 0:
        soma+=n0
    matriz[0].append(n0)
for i in range(0,3):
    n1 = int(input(f"Digite o valor da posicao [1,{i}]: "))
    if n1 % 2 == 0:
        soma+=n1
    matriz[1].append(n1)
for i in range(0,3):
    n2 = int(input(f"Digite o valor da posicao [2,{i}]: "))
    if n2 % 2 == 0:
        soma+=n2
    matriz[2].append(n2)
print("-=-"*16)
print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
print("-=-"*16)
print(f"A soma de todos os valores pares é: {soma}")
print("-=-"*16)
print(f"A soma dos valores da TERCEIRA coluna é: {matriz[0][2]+matriz[1][2]+matriz[2][2]}")
print("-=-"*16)
print(f"E o MAIOR valor da SEGUNDA linha é: {max(matriz[1])}")
print("-=-"*16)