
# Aluna Diana Faustino de Siqueira
# Exercícios aula 06

def calcular_fuso(hora_inicial):
    if hora_inicial == 0:
        hora_inicial = 24
    elif hora_inicial > 24:
        print('Erro')
    else:
        hora_inicial = hora_inicial
    return hora_inicial
hora_inicial = int(input('Insira o horário inicial: '))
hora_viagem = int(input('Insira tempo de viagem: '))
hora_fuso = int(input('Insira seu fuso: '))

final = calcular_fuso(hora_inicial)
resultado = hora_inicial + hora_viagem + hora_fuso
if resultado > 24:
    resultado = resultado - 24
elif resultado < 0:
    resultado = resultado + 24

print(resultado)