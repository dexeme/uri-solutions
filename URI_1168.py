
# Aluna Diana Faustino de Siqueira
# Exercícios aula 08

n = str(input('Insira o número: '))
quantidade = len(n)

um = n.count('1')
dois = n.count('2')
tres = n.count('3')
quatro = n.count('4')
cinco = n.count('5')
seis = n.count('6')
sete = n.count('7')
oito = n.count('8')
nove = n.count('9')
zero = n.count('0')

res = (um*2) + (dois*5) + (tres*5) + (quatro*4) + (cinco*5) + (seis*6) + (sete*3) + (oito*7) + (nove*7) + (zero*6)
print(res)