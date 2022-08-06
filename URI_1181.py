
# Aluna Diana Faustino de Siqueira
# Exercícios aula 14

# Capta linha que será realizada a operação
l = int(input())
# Indicador de operação M ou S
t = input()

# Variável de tamanho da matriz
tamanho = 12
matriz = []

# Preenche cada elemento da matriz
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input()))
    matriz.append(linha)

# Cálculo da soma
soma = 0 
for v in matriz[l]:
    soma += v
resultado = soma

# Cálculo da média
if t == 'M':
    resultado = soma/tamanho

print('{:.1f}'.format(resultado))