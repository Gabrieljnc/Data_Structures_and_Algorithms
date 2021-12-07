
class Aluno:
    def __init__(self, nome, nota_1, nota_2, ):
        self.nome = nome
        self.nota_1 = nota_1
        self.nota_2 = nota_2

    def media(self):
        media_aritmetica = (self.nota_1 + self.nota_2) / 2
        return media_aritmetica

    def mostrar(self):
        print(f"\nNome --> {self.nome}\nNota 1 --> {self.nota_1}\nNota 2 --> {self.nota_2}") 

    def aprov_reprov(self):
        if self.media() >= 6:
            print("Aluno Aprovado")  
        else:
            print("Aluno Reprovado")


aluno1 = Aluno("Gabriel", 8.5, 8)
aluno2 = Aluno("Karina", 5, 5)

media_aluno1 = aluno1.media()
media_aluno2 = aluno2.media()


aluno1.mostrar()
aluno1.aprov_reprov()
aluno2.mostrar()
aluno2.aprov_reprov()
