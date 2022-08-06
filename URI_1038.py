
# Aluna Diana Faustino de Siqueira
# Exercícios aula 02

a = int(input('Insira o código: '))
b = int(input('Insira a quantidade: '))

if a==1:
    r = 4 * b
    print(f'Total: R$ {r}')
elif a==2:
    r = 4.5 * b
    print(f'Total: R$ {r}')
elif a==3:
    r = 5 * b
    print(f'Total: R$ {r}')
elif a==4:
    r = 2 * b
    print(f'Total: R$ {r}')
elif a==5:
    r = 1.5 * b
    print(f'Total: R$ {r}')
else:
    print('Código incorreto')