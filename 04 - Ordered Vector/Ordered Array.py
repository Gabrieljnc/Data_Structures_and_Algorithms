# Biblioteca 

import numpy as np

class Vetor_Ordenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.vetor = np.empty(self.capacidade, dtype = int)

# Imprime

    def Imprimir(self):
        if self.ultima_posicao == -1:
            print("\nVetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, "--", self.vetor[i])

# Insert 

    def Inserir(self, valor_a_inserir):
        if self.ultima_posicao == self.capacidade - 1: # Verificar se o vetor está cheio
            print("\nO vetor está cheio")
            return

        posicao = 0 # Startar variável de controle na primeira posição(primeira execução)
            
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

    def Pesquisa_Linear(self,valor_a_pesquisar):

        for i in range(self.ultima_posicao + 1):

            if self.vetor[i] == valor_a_pesquisar: # Se encontrar
                print("\nValor Encontrado\n")
                return i

            if self.vetor[i] > valor_a_pesquisar: # Se não encontrar
                return -1
        
            if i == self.ultima_posicao: # Se o valor_a_pesquisar for o maior numero
                return -1
    
    def Pesquisa_Binaria(self, valor_a_pesquisar):
        limite_inferior = 0 # Define o limite inferior
        limite_superior = self.ultima_posicao # Define o limite superior
        
        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2) # Define a metade do vetor para selecionar a posicao
            
            if self.vetor[posicao_atual] == valor_a_pesquisar: # se encontrar na primeira tentativa
                return posicao_atual
            
            elif limite_inferior > limite_superior: # se não encontrar
                return -1
            
            else:
                if self.vetor[posicao_atual] < valor_a_pesquisar: # o número está a direita
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1 # o número está a esquerda

    def Excluir(self, valor_a_excluir):
        posicao = self.Pesquisa_Linear(valor_a_excluir) # Realiza a pesquisa do número pra ver se ele ta no vetor
        if posicao == -1: 
            print("Valor não encontrado no vetor - Não foi realizado nenhuma remoção\n")
            return -1
        
        else:
            print("O valor foi encontrado na lista e removido\n")
            for i in range(posicao,self.ultima_posicao): # Remanejamento de posição para substituir o elemento
                self.vetor[i] = self.vetor[i + 1] 

            self.ultima_posicao -= 1 

# Testes 

vetor = Vetor_Ordenado(4)

# Inserindo elementos
vetor.Inserir(3)
vetor.Inserir(5)
vetor.Inserir(12)
vetor.Inserir(10)

# Pesquisar elemento
vetor.Pesquisa_Linear(10)

# Excluir elemento
vetor.Excluir(3)

# Imprimir
vetor.Imprimir()




