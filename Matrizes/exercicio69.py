# Entrar via teclado com doze valores e armazená-los em uma matriz de ordem 3x4. Após a digitação dos valores solicitar uma constante multiplicativa, que deverá multiplicar cada valor matriz e armazenar o resultado em outra matriz de mesma ordem, nas posições correspondentes. Exibir as matrizes na tela, sob a forma matricial, ou seja, linhas por colunas.

matriz = [  [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]  ]

for l in range(0, 4, 1):
    for c in range(0, 3, 1):
        matriz[l][c] = int(input('Digite um numero: '))
    
        
multiplica = int(input("Digite uma constante multiplicativa: "))

print("Matriz original:")
for i in range(0, 4, 1):
    print(matriz[i])

print()

for l in range(0, 4, 1):
    for c in range(0, 3, 1):
        matriz[l][c] = matriz[l][c] * multiplica

print("Matriz multiplicada:")
for i in range(0, 4, 1):
    print(matriz[i])