
# Aluna Diana Faustino de Siqueira
# Exercícios aula 06

def calcular():
    soma = 0
    quantidade = 0

    while True:
        idade = int(input('Insira as idades.\nDigite um número negativo para parar: '))

        if idade < 0:
            break

        soma += idade
        quantidade += 1

    print(f'{soma / quantidade:.2f}')

calcular()