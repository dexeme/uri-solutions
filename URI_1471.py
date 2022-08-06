
# Aluna Diana Faustino de Siqueira
# Exercícios aula 15

nadaram = set()
n,r = [int(x) for x in input().split()]

while r < 0 or r > 10000:
    n,r = [int(x) for x in input('Insira de novo: ').split()]

while n < 0 or n > 10000:
    n,r = [int(x) for x in input('Insira de novo: ').split()]

for pessoa in range(1,n+1):
    nadaram.add(pessoa)

if r == 0:
    print('*')

sr = [int(x) for x in input().split()]
retornatam = set(sr)

if len(nadaram.difference(retornatam)) == 0:
    print('*')
else:
    print(*nadaram.difference(retornatam), sep=" ")