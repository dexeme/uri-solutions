
# Aluna Diana Faustino de Siqueira
# Exercícios aula 08

carac = input()
res = 0

if carac[1].isupper():
    res = int(carac[2]) - int(carac[0])
else:
    res = int(carac[2]) + int(carac[0])

if int(carac[0]) == int(carac[2]):
    res = int(carac[0])/int(carac[2])

print(res) 
