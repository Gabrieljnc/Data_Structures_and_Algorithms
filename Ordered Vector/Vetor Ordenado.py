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
            print("O vetor está cheio")
            return

        posicao = 0 # Startar variável de controle (primeira posicao)
            
        for i in range(self.ultima_posicao + 1): # Percorrer os itens do vetor
            posicao = i # Vai atribuir o index que o numero vai ser alocado de acordo com as iterações
            if self.vetor[i] > valor_a_inserir: # Se o valor do vetor for maior que o valor a inserir
                break
                                              
            if i == self.ultima_posicao: # Se passar por todos elementos e o i == ultima_posicao, deve-se colocar o elemento na frente
                posicao = i + 1 

        ultima_posicao = self.ultima_posicao # Variável de controle da ultima posição

        # Percorrer de tras pra frente
        while ultima_posicao >= posicao: # a ultima_posicao tem que ser menor do que a posicao(local onde numero será inserido) para abrir espaço para o numero ser inserido
            self.vetor[ultima_posicao + 1] = self.vetor[ultima_posicao] # Remanejar para uma casa a frente
            ultima_posicao -= 1

        self.vetor[posicao] = valor_a_inserir # Atribuição do valor à posição 
        self.ultima_posicao += 1 # Incrementa a ultima_posição, pois foi add um novo numero

    def pesquisar(self,valor_a_pesquisar):

        for i in range(self.ultima_posicao + 1):

            if self.vetor[i] == valor_a_pesquisar: # Se encontrar
                return i

            if self.vetor[i] > valor_a_pesquisar: # Se não encontrar
                return -1
        
            if i == self.ultima_posicao: 
                return -1

    def excluir(self, valor_a_excluir):
        posicao = self.pesquisar(valor_a_excluir)
        if posicao == -1:
            return -1
        
        else:
            for i in range(posicao,self.ultima_posicao):
                self.vetor[i] = self.vetor[i + 1]

            self.ultima_posicao -= 1


vetor = Vetor_Ordenado(4)

vetor.Inserir(3)
vetor.Inserir(5)
vetor.Inserir(12)
vetor.Inserir(10)

vetor.pesquisar(13)
# vetor.excluir(3)
vetor.Imprime()




