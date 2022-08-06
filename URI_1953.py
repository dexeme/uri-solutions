
# Aluna Diana Faustino de Siqueira
# Exercícios aula 18

continuar = 'S'
while continuar == 'S':
    matriculados = []
    total_epr = 0
    total_ehd = 0
    total_intrusos = 0
    n = int(input('Numéro de alunos: '))

    while n < 1 or n > 100000:
        n = int(input('O número deve estar entre 1 e 100000: '))

    for i in range (n):
        j,sigla_input = [str(x) for x in input().upper().split()]
        dicionario_matriculados = {'x':j, 'sigla_input':sigla_input}
        matriculados.append(dicionario_matriculados)

    for i in matriculados:
        if i['sigla_input'] == 'EPR':
            total_epr += 1
        elif i['sigla_input'] == 'EHD':
            total_ehd += 1
        else:
            total_intrusos += 1
    print(f'EPR: {total_epr}')
    print(f'EHD: {total_ehd}')
    print(f'INTRUSOS: {total_intrusos}')
    continuar = input('Deseja continuar? [S/N]\n>>>   ').upper()
print('Fim do programa :D')