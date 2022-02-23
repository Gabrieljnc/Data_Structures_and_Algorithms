import numpy as np 
from colorama import Fore


class Fila_prioridade():
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.fila = np.empty(self.capacidade, dtype = int)

    
    def fila_vazia(self):
        return self.numero_elementos == 0

    def fila_cheia(self):
        return self.numero_elementos == self.capacidade 

    def enfileirar(self, valor_a_enfileirar):

        if self.fila_cheia():
            print("Fila está cheia")
            return 
        
        if self.numero_elementos == 0:
            self.fila[self.numero_elementos] == valor_a_enfileirar
            self.numero_elementos += 1 

        else:

            x = self.numero_elementos - 1 

            while x >= 0:
                if valor_a_enfileirar > self.fila[x]:
                    self.fila[x + 1] = self.fila[x] 
                else:
                    break
                x -= 1

            self.fila[x + 1] = valor_a_enfileirar
            self.numero_elementos += 1

    def desinfileirar(self):
        if self.fila_vazia():
            print("Fila está vazia")
            return 

        valor = self.fila[self.numero_elementos - 1 ]

        self.numero_elementos -= 1
        return valor

    def primeiro_elemento(self):
        if self.fila_vazia():
            print("Fila está vazia")
            return -1 
        
        print(f"\n {Fore.BLUE} O primeiro elemento da fila de prioridade é {self.fila[self.numero_elementos -1]}\n")
        return self.fila[self.numero_elementos -1]

fila = Fila_prioridade(5)

fila.enfileirar(3)
fila.enfileirar(7)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(1)

fila.primeiro_elemento()