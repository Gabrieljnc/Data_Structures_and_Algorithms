
print('Exercicio 2 - IF/ELSE - Básico Python')

M1 =  float(input(f"Digite a Nota 1 -->  "))
M2 =  float(input(f"Digite a Nota 2 -->  "))
M3 =  float(input(f"Digite a Nota 3 -->  "))

Media_aritm = (M1 + M2 + M3) / 3

if (Media_aritm >= 0.0) & (Media_aritm <=4.0):
    print("O aluno foi reprovado")

elif (Media_aritm >= 4.1) & (Media_aritm <= 6.0):
    print("Pegou o exame")

    nota_exame = float(input("Digite a nota do exame -->  "))

    if nota_exame > 6.0:
        print("Aprovado")
    else:
        print("Reprovado")

elif Media_aritm > 6.0:
    print("Aprovado")

else:
    print("Rode o programa novamente")