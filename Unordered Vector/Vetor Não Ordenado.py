# Bibliotecas utilizadas

import numpy as np

class Vetor_nao_Ordenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade # Capacidade suportada pelo Vetor 
        self.ultima_posicao = -1     # Variavel que controla a última posição do vetor
        self.vetor = np.empty(self.capacidade, dtype= int) # Criação do vetor vazio

# Função Mostrar valores
    def mostrar(self):
        if self.ultima_posicao == -1: 
            print("Vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1): # Percorre todos elementos do vetor 
                print(i, "---", self.vetor[i]) # Printa o index e o elemento correspondente no vetor


# Função Inserir
    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1: # Ex: capacidade = 5 tem como ultima posição 4, pois a posição começa a partir do 0
            print("O vetor está cheio")
        else:
            self.ultima_posicao += 1 # Incrementa posição para representar o index do valor e mudar o novo elemento na ultima posição
            self.vetor[self.ultima_posicao] = valor # Index do vetor [representado pela variável ultima posicao] = valor escolhido pelo usuário

# Função Pesquisar
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1): # Percorre os elementos do vetor 
            if valor == self.vetor[i]: # Se o valor procurado for igual ao valor no vetor
                return i 
        return -1 # Retorna -1 caso não encontre o valor 

# Função Remover
    def remover(self, valor):
        posicao = self.pesquisar(valor) # Realiza a pesquisa pra ver se o valor está no vetor
        if posicao == -1: # -1 retorno da função pesquisar
            print("Não possui esse elemento no vetor")

        else:
            for i in range(posicao, self.ultima_posicao): # Percorre da posição do elemento encontrado até a ultima posição
                self.vetor[i] = self.vetor[i + 1] # Antiga posição --> Nova posição (Remanejamento de posição dos elementos)

            self.ultima_posicao -= 1

# Testing the code

vetor = Vetor_nao_Ordenado(5)

vetor.inserir(10)
vetor.inserir(20)
vetor.inserir(30)
vetor.inserir(40)
vetor.inserir(50)
vetor.mostrar()
vetor.pesquisar(30)
vetor.remover(30)