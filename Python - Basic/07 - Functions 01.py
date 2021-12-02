def Ler_temperatura():
    celsius = float(input("\nDigite o valor da temperatura em Celsius --> "))
    return celsius

def Converte_C_to_F(celsius):
    temperatura_farenheit = (9 * celsius + 160) / 5
    return temperatura_farenheit

def Mostrar(temperatura_farenheit):
    print(temperatura_farenheit)


# Atribui a variável temperatura_celsius a função com input de ler a temperatura
temperatura_celsius = Ler_temperatura()

# Converte de acordo com a temperatura lida
temperatura_farenheit = Converte_C_to_F(temperatura_celsius)

# printa o valor da temperatura já convertida
Mostrar(temperatura_farenheit)