
# Aluna Diana Faustino de Siqueira
# Exercícios aula 17

conta = 0
frutas = []
n = int(input())
m = int(input())

for i in range(m):
    nome,preco = input().split()
    feira = {'nome':nome,'preco':float(preco)}
    frutas.append(feira)

p = int(input())

for j in range(p):
    nome,quantidade = input().split()
    quantidade = int(quantidade)

    for k in frutas:
        if k['nome'] == nome:
            conta += k['preco']*quantidade
print(f'R$ {conta:.2f}')