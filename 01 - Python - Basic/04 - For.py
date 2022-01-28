print('Exercicio 1 - FOR/WHILE - Básico Python')
print("\n Faça uma programa que Leia 5 notas e informe a média utilizando - For \n")


nota_total = 0

for i in range(0,5):
   nota = float((input("Digite sua nota -->   ")))
   
   nota_total += nota

media = nota_total / 5

print(f"\nA nota media final é --> {media} \n")
