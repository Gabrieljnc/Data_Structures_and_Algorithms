print('\n Exercicio 1 - INPUT - Básico Python')

km_por_litro = 12

tempo_viagem = float(input('Digite o tempo da viagem '))

velocidade_media = float(input('Digite a velocidade media da viagem '))

distancia = tempo_viagem * velocidade_media

litros_usados = distancia / km_por_litro

print(f'A velocidade média é --> {velocidade_media}'+ '\n' + f'O tempo gasto na viagem é de --> {tempo_viagem}' + '\n' + f'A distância percorrida foi de --> {distancia}' '\n' + f'A quantidade de litros usada foi --> {round(litros_usados, 2)}')