print('Exercicio 1 - FOR /WHILE - Básico Python')
print("\n Faça uma programa que Leia 4 notas e informe a média utilizando - While \n")


nota_total = contador = 0

while contador < 5:
    nota = int(input("Digite sua nota -->  "))

    contador += 1

    nota_total  += nota

media = nota_total / 5

print(f"A nota media final é --> {media} \n")

