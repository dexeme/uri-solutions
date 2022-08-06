
# Aluna Diana Faustino de Siqueira
# Exercícios aula 14

# Capta se sera realizada a soma ou a média
o = input()
soma = 0
linha = 0
valor = 0

# Como essa o valor é cravado em 12, eu não fiz uma variável de tamanho
# Para toda linha de 0 até 11
for i in range(12):
    linha = i
    for j in range(12):
        valor = float(input())
        if j < linha:
            soma = soma + valor
            valor = valor + 1

# Se o usuário quiser a soma, apenas vai printar a soma
if o == 'S':
    print("%.1f" % soma)
# Se não quiser a soma, vai printar a média da soma/vezes que apareceu
else:
    print("%.1f" % (soma/valor))
