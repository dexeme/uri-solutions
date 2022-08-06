
# Aluna Diana Faustino de Siqueira
# Exercícios aula 07

alunos = int(input('Insira a quantidade de alunos: '))
computadores  = int(input('Insira o total de computadores: '))
queimados  = int(input('Insira o total de computadores queimados por Caio: '))
compilador  = int(input('Insira o total de computadores sem compilador: '))

if computadores - 1 - queimados - compilador >= alunos:
    print('Igor feliz')
elif computadores - 1 - queimados - compilador < alunos:
    print('Igor Bolado')
elif queimados > (compilador/2):
    print('Caio a culpa é tua!')