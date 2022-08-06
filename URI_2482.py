
# Aluna Diana Faustino de Siqueira
# Exercícios aula 18


def etiquetas(mensagem1,criancas1):
    for c in criancas1:
        print(c['nome'])
    for msg in mensagem1:
        if c['idioma'] == msg['idioma']:
            print(msg['traducao'])
            print('')

crianca = []
cartas = []
n = int(input())
while n < 1 or n > 100:
    n = int(input('Insira novamente: '))

for i in range(n):
    idioma = str(input('Digite o idioma: ')).lower()
    traducao = str(input('Digite a tradução: '))
    mensagem = {'idioma':idioma, 'traducao':traducao}
    cartas.append(mensagem.copy())
print(cartas)

m = int(input())

while m < 1 or m > 100:
    m = int(input())
    
    
for c in range(m):
    crianca_nome = str(input())
    crianca_idioma = str(input().lower())
    criancas_dic = {'nome':crianca_nome, 'idioma':crianca_idioma}
    crianca.append(criancas_dic)
    
etiquetas(cartas,crianca)