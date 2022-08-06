
# Aluna Diana Faustino de Siqueira
# Exercícios aula 08

contador = 0
volta = 360
inp_comp = 0

comandos = int(input('Comandos: '))
for i in range (0, comandos):
    contador += 1
    print(f'Insira a {contador}º direção [D/E]')
    inp_com = str(input('Selecionar > '))
    while inp_com not in "DdEe":
        inp_com = str(input('Você digitou uma opção errada, por favor tente novamente: ')).upper()
        inp_com = input()
    if inp_com == "D" or inp_com == "d":
        volta = volta + 90
    elif inp_com == "E" or inp_com == "e":
        volta = volta - 90
    if volta > 360:
        volta = volta - 360

if volta == 360:
    print('Norte')
elif volta == 270:
    print('Oeste')
elif volta == 180:
    print('Sul')
elif volta == 90:
    print('Leste')