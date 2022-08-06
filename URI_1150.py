
# Aluna Diana Faustino de Siqueira
# Exercícios aula 06

x = int(input('Insira o valor de X'))
z = x - 1

i = 2
soma = x
s=1
while z <= x:
    z = int(input('Insira o valor de Z: '))
 
while soma <= z:
    soma = soma +  x + s
   
    if soma <= z:
        i = i + 1
        s=s+1
print(i)