
# Aluna Diana Faustino de Siqueira
# Exercícios aula 16

continuar = 'S'

while continuar == 'S':
    print('---------------\n')
    t = int(input('Casos de teste: '))

    while t < 1 or t > 5000:
        t = int(input('Insira novamente, por favor: '))

    p,n = [int(x) for x in input('Número de provas e número de alunos: ').split()]

    while p > 5 or p < 2 or n < 2 or n > 50:
        
        p,n = [int(x) for x in input('Insira novamente o número de provas e número de alunos: ').split()]


    for c in range (n):
        nota_valida = True
        nota_aluno = [float(x) for x in input(f'Digite as {p} notas: ').strip().split()]
        for nota in nota_aluno:
            if nota > 10 or nota < 0:
                nota_valida = False
        while not nota_valida:
            nota_valida = True
            nota_aluno = [float(x) for x in input(f'Digite novamente as {p} notas: ').strip().split()]
            for nota in nota_aluno:
                if nota > 10 or nota < 0:
                    nota_valida = False


        while len(nota_aluno) != p:
            nota_aluno = [float(x) for x in input(f'Insira novamente as {p} notas, por favor:\n').strip().split()]
        while not (0 <= nota_aluno[c] <= 10):
            nota_aluno = [float(x) for x in input(f'Insira novamente as {p} notas, por favor:\n').strip().split()]
        if sum(nota_aluno)/p >= 7.0:
            media = max(nota_aluno)
            print('{:.2f}\n'.format(media))
        elif sum(nota_aluno)/p < 7.0 and sum(nota_aluno)/p >= 4.0:
            media = sum(nota_aluno)/p
            print('{:.2f}\n'.format(media))
        elif sum(nota_aluno)/p < 4.0:
            media = sum(nota_aluno)/p
            print('{:.2f}\n'.format(media))        

    continuar = input('Deseja continuar? [S/N]\n>>>   ').upper()
('Fim do programa')

