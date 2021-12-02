dict = {}

for i in range(1,4):
    chave = str(input("\nDigite o nome da pessoa -->  "))
    valor = float(input("Digite sua nota -->  "))
    print("---------------------------------")
    dict[chave] = valor
print(f"\n Elementos add no dict {dict}")

soma = 0 
for value in dict.values():
    soma += value

media_final = soma / 3

print(f"\nA média das notas foi de {media_final :.2f}")