# Biblioteca 

import numpy as np

class Vetor_Ordenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.vetor = np.empty(self.capacidade, dtype = int)

# Imprime

    def Imprime(self):
        if self.ultima_posicao == -1:
            print("Vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, "--", self.vetor[i])

# Insert 

    def Inserir(self, valor_a_inserir):
        if self.ultima_posicao == self.capacidade - 1: # Verificar se o vetor está cheio
            print("The array is full")
            return

        posicao = 0 # Startar variável de controle
            
        for i in range(self.ultima_posicao + 1): # Percorrer os itens do vetor
            posicao = i # Vai atribuir o index de acordo com as iterações
            if self.vetor[i] > valor_a_inserir: # Se o valor correspondente ao index[i] for maior que o valor a inserir
                break

            if i == self.ultima_posicao: # Se passar por todos elementos e o ultimo ainda for menor, deve-se colocar o elemento na frente
                posicao = i + 1 

        ultima_posicao = self.ultima_posicao # Variável de controle da ultima posição

        while ultima_posicao >= posicao: 
            self.vetor[ultima_posicao + 1] = self.vetor[ultima_posicao] # Remanejar para uma casa a frente
            ultima_posicao -= 1

        self.vetor[posicao] = valor_a_inserir # Atribuição do valor à posição 
        self.ultima_posicao += 1 # Incrementa a ultima posição

vetor = Vetor_Ordenado(4)





