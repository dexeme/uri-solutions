
# Aluna Diana Faustino de Siqueira
# Exercícios aula 02

C = int(input("Informe a quantia de competidores: "))
while C <= 1 and C >= 1000:
    C = int(input("Numero invalido, informe-o novamente: "))

P = int(input("Informe a quantia de folhas compradas: "))
while P <= 1 and P >= 1000:
    P = int(input("Numero invalido, informe-o novamente: "))

F = int(input("Informe a quantia de folhas por aluno: "))
while F <= 1 and F >= 1000:
    F = int(input("Numero invalido, informe-o novamente: "))

if C * F <= P:
    print("S")
else:
    print("N")