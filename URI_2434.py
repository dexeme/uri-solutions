
# Aluna Diana Faustino de Siqueira
# Exercícios aula 07

n, s = input().split()
n = int(n)
s = int(s)

menor_saldo = s

for i in range(n):
    movimentacao = int(input())
    s += movimentacao

    if s < menor_saldo:
        menor_saldo = s

print(menor_saldo)