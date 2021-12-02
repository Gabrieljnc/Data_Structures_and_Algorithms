lista_armazenamento = []
soma = 0

for i in range(1,6):
    numero = int(input("\nDigite um numero --> "))
    lista_armazenamento.append(numero)

for number in lista_armazenamento:
    soma += number
    
print(soma)