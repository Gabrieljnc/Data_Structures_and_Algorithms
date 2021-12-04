import re

# Search Function

phrase_1 = "Olá, meu número de  telefone é (61)98258-9107"
search_1 = re.search("\(\d{2}\)\d{4,5}-\d{4,5}", phrase_1)
print(search_1)


phrase_2 = "A placa do carro que eu anotei durante o acidente foi FrT-1998"
search_2 = re.search("[A-Za-z]{3}-\d{4}", phrase_2)
print(search_2)

phrase_3 = "Entre em contato meu email é teste@test.com.br"
                #palavra + @ + palavra + ponto + 3 letras + ponto + 2 letras
search_3 = re.search("\w+@\w+\.[a-z]{3}\.[a-z]{2}", phrase_3)
print(search_3)

# Match Function -- Identify only in the beginning of string 

phrase_4 = "Olá, meu número de  telefone é (61)98258-9107" # Dont match
phrase_4_2 = "(61)98258-9107 é meu telefone"               # Match
match_1 = re.match("\(\d{2}\)\d{4,5}-\d{4,5}", phrase_4_2)
print(match_1)

phrase_5 = "Olá, meu número de  telefone é (61)98258-9107, e eu tenho outro numero (61)98222-7919"
findall_1 = re.findall("\(\d{2}\)\d{4,5}-\d{4,5}", phrase_5)
print(findall_1)