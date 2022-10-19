# Fazer um programa para criar uma matriz de 3X3. Solicitar ao usuário que digite os 9 números para armazenar na matriz. Após isso exibir os números armazenados na matriz

matriz = [ [0,0,0], 
           [0,0,0], 
           [0,0,0] ]
 
for l in range(0, 3, 1):
    for c in range(0, 3, 1):
        matriz[l][c] = int(input('Digite um numero: '))
 
# Mostra a matriz um uma linha única
print(matriz)
 
# Mostra a matriz de forma real
for i in range(0, 3, 1):
    print(matriz[i])
 
# Mostra cada valor da matriz
for l in range(0, 3, 1):
    for c in range(0, 3, 1):
        print(matriz[l][c])