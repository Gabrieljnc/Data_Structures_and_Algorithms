import numpy as np 

class Fila_Circular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0 # Variável que guarda o indice do primeiro elemento da fila
        self.final = -1 # Variável que guarda o indice final elemento da fila
        self.numero_elementos = 0 # Numero de elementos na fila
        self.fila = np.empty(self.capacidade, dtype = int)

    # Função que verifica se a fila está vazia
    def _fila_vazia(self): 
        return self.numero_elementos == 0 

    # Função que verifica se a fila está cheia
    def _fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def mostrar_todos_elementos(self):
        if self._fila_vazia():
            print("A fila está vazia")
            return -1 
        else:
            for i in range(self.capacidade):
                print(i, "-->", self.fila[i])

    # Função que enfileira os elementos na fila
    def enfileirar(self, valor_a_enfileirar):
        if self._fila_cheia():
            print("Fila está cheia")
            return 

        if self.final == self.capacidade -1: # Se chegar no fim da fila e não tive mais capacidade
            self.final = -1 # Joga o final para o indice do inicio

        self.final += 1
        self.fila[self.final] = valor_a_enfileirar
        self.numero_elementos += 1

    def desenfileirar(self):
        if self._fila_vazia():
            print("A fila está vazia")
            return
        
        temp = self.fila[self.inicio] # Variável para retornar o valor que será desenfilerado
        self.inicio += 1 # Como sera desenfileirado o indice de numero irá para o numero da frente
        
        if self.inicio == self.capacidade -1:
            self.inicio = 0
        
        self.numero_elementos -= 1
        return temp

    def primeiro_elemento(self):
        if self._fila_vazia():
            print("Fila está Vazia")
            return -1
        print(self.fila[self.inicio])
        return self.fila[self.inicio]


# Definindo a fila com a capacidade de 5 elementos
fila = Fila_Circular(5)

# Enfileirando os 5 elementos na fila

fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
fila.enfileirar(40)
fila.enfileirar(50)

# Vendo o primeiro elemento da fila = 10

fila.primeiro_elemento()

# Desenfilera o primeiro elemento

fila.desenfileirar() 

# Vendo o primeiro novo elemento da fila = 20
fila.primeiro_elemento()

# Adicionando o numero 60 na fila
fila.enfileirar(60)

# Tentando adicionar um número maior do que a capacidade da fila
fila.enfileirar(70)

# Mostrando todos elementos

fila.mostrar_todos_elementos()