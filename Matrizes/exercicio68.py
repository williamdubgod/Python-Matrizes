# Entrar via teclado com doze valores e armazená-los em uma matriz de ordem 3x4. Após a digitação dos valores solicitar uma constante multiplicativa, que deverá multiplicar cada valor matriz e armazenar o resultado na própria matriz, nas posições correspondentes.

matriz = [  [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]  ]

for l in range(0, 4, 1):
    for c in range(0, 3, 1):
        matriz[l][c] = int(input('Digite um numero: '))
        
multiplica = int(input("Digite uma constante multiplicativa: "))

for l in range(0, 4, 1):
    for c in range(0, 3, 1):
        matriz[l][c] = matriz[l][c] * multiplica

for i in range(0, 4, 1):
    print(matriz[i])
