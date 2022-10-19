# Armazenar seis nomes em uma matriz de ordem 2x3. Apresentar os nomes na tela.

matriz = [ ['','',''], 
           ['','',''], ]

for l in range(0, 2, 1):
    for c in range(0, 3, 1):
        matriz[l][c] = input('Digite um nome: ')

for i in range(0, 2, 1):
    print(matriz[i])