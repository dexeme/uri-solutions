
# Aluna Diana Faustino de Siqueira
# Exercícios aula 06

def calcular_aumento(salario):
    if 0 <= salario <= 400.00:
        salario = salario + (salario*.15)
    elif 400.01 <= salario <= 800.00:
        salario = salario + (salario*.12)
    elif 800.01 <= salario <= 1200.00:
        salario = salario + (salario*.10)
    elif 1200.00 <= salario <= 2000.00:
        salario = salario + (salario*.07)
    elif salario > 1200.00:
        salario = salario + (salario*.04)
    return salario
salario = float(input('Insira seu salário: '))
total_salario =  calcular_aumento(salario)
reaj = (total_salario-salario)
perc = ((total_salario*100) / salario ) - 100
print(f'Novo salário: {total_salario:.2f}\nReajuste ganho {reaj:.2f}\nEm percentual: {perc:.0f}%')