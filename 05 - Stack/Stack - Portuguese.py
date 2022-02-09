import numpy as np 

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade # Capacidade total da pilha
        self.topo = -1 # Variável de controle de posição dos elementos da pilha
        self.pilha = np.empty(self.capacidade, dtype = int)

    # Função para verificar se a pilha está vazia
    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else: 
            return False
    
    # Função para verificar se a pilha ultrapassou a capacidade
    def pilha_cheia(self):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False

    # Função para empilhar elementos 
    def empilhar(self, valor_a_empilhar):
        if self.pilha_cheia():
            print("Pilha está cheia")
        else:
            self.topo += 1 
            self.pilha[self.topo] = valor_a_empilhar

    # Função para desempilhar elementos
    def desempilhar(self):
        if self.pilha_vazia():
            print("Pilha está Vazia")
        else:
            self.topo -= 1
    
    # Função para ver o elemento que está no topo
    def ver_elemento_top(self):
        if self.topo != -1:
            print(self.pilha[self.topo])
            return self.pilha[self.topo]
        else:
            return -1

            
# Aplicando o código
pilha = Pilha(5)

pilha.empilhar(7)
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)

pilha.desempilhar()

pilha.ver_elemento_top()