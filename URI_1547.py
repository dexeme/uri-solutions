
# Aluna Diana Faustino de Siqueira
# Exercícios aula 11

casos = int(input())
for i in range (casos):
    alunos, n = [int(x) for x in input().split()]
    contador = alunos + 1
    i = 0
    if 4 <= alunos <= 10 and 1 <= n <= 100:
        tentativas = [int(x) for x in input().split()] 
        if n in tentativas: 
            while variavel == alunos+1:
                if n == tentativas[i]:
                    variavel = tentativas.index(tentativas[i]) + 1
                i +=1
            print(variavel)        
        else: 
            menordif = abs(n - tentativas[0])
            maisproximo = 0 
            for x in range(1, alunos):
                if abs(n - tentativas[x]) < menordif:
                    menordif = abs(n - tentativas[x])
                    maisproximo = x
            print(maisproximo + 1)    