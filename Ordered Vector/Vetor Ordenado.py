import numpy as np

class Vetor_Ordenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.vetor = np.empty(self.capacidade, dtype= int)
        self.ultima_posicao = -1

    def Imprime(self):
        if self.ultima_posicao == -1:
            print("Vetor está vazio") 
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, "--", self.vetor[i])

    def Inserir(self,valor_a_inserir):
        if self.ultima_posicao == self.capacidade -1:
            print("O vetor está cheio")
            return

        posicao = 0

        for i in range(self.ultima_posicao + 1):
            posicao = i
            
            if self.vetor[i] > valor_a_inserir:
                break

            if i == self.ultima_posicao:
                posicao = i + 1

        ultima_posicao = self.ultima_posicao

        while ultima_posicao >= posicao:
            self.vetor[ultima_posicao + 1] = self.vetor[ultima_posicao]
            ultima_posicao -= 1

        self.vetor[posicao] = valor_a_inserir
        self.ultima_posicao += 1

    def Pesquisar(self, valor_a_pesquisar):

        for i in range(self.ultima_posicao + 1):

            if self.vetor[i] == valor_a_pesquisar:
                print(f"Valor Encontrado na posição {i}")
                return i 

            if self.vetor[i] > valor_a_pesquisar:
                print("Valor não encontrado")
                return -1 

            if i == self.ultima_posicao:
                print("Valor não encontrado")
                return -1

    def Excluir(self, valor_a_excluir):
        posicao = self.Pesquisar(valor_a_excluir)

        if posicao == -1:
            print("Numero nao existe no vetor")
            return -1

        else:
            for i in range(posicao, self.ultima_posicao):
                self.vetor[i] = self.vetor[i + 1]

            self.ultima_posicao -= 1

array = Vetor_Ordenado(5)

array.Inserir(2)
array.Inserir(3)
array.Inserir(5)
array.Inserir(4)
array.Inserir(22)

array.Excluir(22)

array.Pesquisar(4)
array.Imprime()
