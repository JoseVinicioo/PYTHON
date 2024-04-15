# matriz = [[],[],[]]
# for i in range(0,3):
#     matriz[0].append(int(input(f"Digite o valor da posicao [0,{i}]: ")))
# for i in range(0,3):
#     matriz[1].append(int(input(f"Digite o valor da posicao [1,{i}]: ")))
# for i in range(0,3):
#     matriz[2].append(int(input(f"Digite o valor da posicao [2,{i}]: ")))
# print("-=-"*5)
# print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")

matriz = [[0,0,0],[0,0,0],[0,0,0]] 
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor prar [{l},{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()