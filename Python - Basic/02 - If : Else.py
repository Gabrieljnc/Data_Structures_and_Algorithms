print('Exercicio 1 - IF/ELSE - Básico Python')

idade = int(input(f"Digite sua Idade "))

if (idade >= 0) & (idade <= 12):
    print("Criança")

elif (idade >=13) & (idade <=17):
    print("Adolescente")

elif (idade >= 18):
    print("Adulto")

else:
    print("Idade é negativa")