
# Aluna Diana Faustino de Siqueira
# Exercícios aula 07

inicio = int(input('Insira a hora inicial: '))
final  = int(input('Insira a hora final: '))
horas = 0

if inicio < final:
    horas = final - inicio
elif inicio > final:
    horas = (24 - inicio) + final
else:
    horas = 24
print(f'A quantidade total de horas é de {horas} horas')