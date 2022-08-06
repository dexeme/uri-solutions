
# Aluna Diana Faustino de Siqueira
# Exercícios aula 08

quant = int(input('Quantidade: '))

res_s = res_r = res_c = 0

for i in range (0,quant):
    quantidade, letra = input().split()
    sapo = letra.count('S')
    rato = letra.count('R')
    coelho = letra.count('C')

    res_s += (sapo * int(quantidade)) 
    res_r += (rato * int(quantidade))
    res_c += (coelho * int(quantidade))

total = res_c+res_r+res_s
print(f'TOTAL {res_c+res_r+res_s}')
print(f'Total coelhos: {res_c}')
print(f'Total sapos: {res_s}')
print(f'Total ratos: { res_r}')

print(f'Percentual coelhos: {res_c * 100 / total}%')
print(f'Percentual sapos: {res_s * 100 / total}%')
print(f'Percentual ratos: {res_r * 100 / total}%')