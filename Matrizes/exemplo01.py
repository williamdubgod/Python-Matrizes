# Fazer um programa para criar uma matriz de 3X3, com números fixos. Após isso exibir os números armazenados na matriz

matriz = [ [1,2,3], [4,5,6], [7,8,9] ]

print(matriz)
 
for i in range(0, 3, 1):
    print(matriz[i])

for l in range(0, 3, 1):
    for c in range(0, 3, 1):
        print(matriz[l][c])
 
