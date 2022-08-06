
# Aluna Diana Faustino de Siqueira
# Exercícios aula 02

def triangulo_valido(a,b,c):
    if(a+b>c and a+c>b and b+c>a): 
        return True
    else:
        return False

a = float(input('Insira o valor a: '))
b = float(input('Insira o valor b: '))
c = float(input('Insira o valor c: '))

if triangulo_valido(a, b, c):
    print(f'Perímetro: {a+b+c}')
else:
    print(f'Área: {((a+b)*c) / 2}')