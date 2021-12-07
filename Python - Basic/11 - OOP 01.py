
# Classe / Molde-Base
class Triangulo: 
    def __init__(self, lado_1, lado_2, lado_3, base, altura): # Método Init (Função Construtora)
    # Atributos
        self.lado_1 = lado_1 
        self.lado_2 = lado_2
        self.lado_3 = lado_3
        self.base = base
        self.altura = altura

    # Métodos

    def area(self):
        return (self.base * self.altura) / 2

    def tipo_triangulo(self):
        if self.lado_1 > (self.lado_2 + self.lado_3):
            return "\nnão é triângulo"
        
        elif (self.lado_1 == self.lado_2) or (self.lado_1 == self.lado_3) or (self.lado_2 == self.lado_3):
            return "\nisosceles"

        else:
            return "\noutro tipo de triângulo"

# Objetos
t1 = Triangulo(2, 1, 3, 4, 3) 
t2 = Triangulo(8, 8, 8, 16, 9)

# Acessar atributos
print(t1.lado_1, t1.lado_2, t1.lado_3, t1.base, t1.altura)
print(t2.lado_2, t2.lado_2, t2.lado_3, t2.base, t2.base)

print(t1.area())
print(t1.tipo_triangulo())
print(t2.tipo_triangulo())