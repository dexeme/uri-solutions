
# Aluna Diana Faustino de Siqueira
# Exercícios aula 07

def is_primo(n):
    div = 0

    for i in range(1, n + 1):
        if n % i == 0:
            div += 1

    return div == 2


def primo_mais_proximo(n):
    for i in range(n, 0, -1):
        if is_primo(i):
            return i


n, m = input().split()
n = int(n)
m = int(m)

p1 = primo_mais_proximo(n)
p2 = primo_mais_proximo(m)

print(p1 * p2)
