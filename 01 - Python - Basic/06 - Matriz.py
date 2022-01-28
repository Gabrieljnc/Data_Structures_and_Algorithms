import numpy as np

soma = 0 # Controlador de soma  

matriz = np.array([[3, 4, 1],  # Geração de matriz 
                   [3, 1, 5]])

for linha in range(matriz.shape[0]): # Percorrer linha
    for coluna in range(matriz.shape[1]):  # Percorrer coluna
        soma += matriz[linha][coluna] # guardar na variavel soma --> soma + o elemento [j] dentro de [i]

print(soma)

 