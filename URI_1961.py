
# Aluna Diana Faustino de Siqueira
# Exercícios aula 15

alturas_cano = []
p,n = [int(x) for x in input().split()]
cano = [int(x) for x in input().strip().split()]
aa = 0

voce_ganhou = True
for c in range (0, len(cano)):
    if cano[c] <= p + aa:
        aa = cano[c]
    else:
        voce_ganhou = False
        break
if voce_ganhou:
    print('You win')
else:
    print('Game Over')