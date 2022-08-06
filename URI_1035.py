
# Aluna Diana Faustino de Siqueira
# Exercícios aula 02

a = int(input('Insira o valor a: '))
b = int(input('Insira o valor b: '))
c = int(input('Insira o valor c: '))
d = int(input('Insira o valor d: '))
cond_1 = 0

if b>c and d>a and c+d > a+b and c > 0 and d > 0 and (a%2) == 0:
    cond_1 = 1
if cond_1 == 1:
    print('Valores aceitos')
else:
    print('Valores não aceitos')