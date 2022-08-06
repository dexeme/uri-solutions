
# Aluna Diana Faustino de Siqueira
# Exercícios aula 14

total_pessoas = int(input('Insira o total de pessoas: '))
opinioes = []
# Contabiliza os votos numa linha só
voto = input().strip().split()
# Coloca os valores de voto na lista opinioes
opinioes.append(voto)
# Conta a quantidade de votos de cada tipo
um = voto.count(1)
zero = voto.count(0)

# Se tiver mais negativos que positivos, imprime N
if um > len(opinioes):
    print('N')
# Se tiver mais positivos que negativos, imprime S
elif um < len(opinioes):
    print('S')
# Se os dois valores forem iguais, imprime N também
else:
    print('N')