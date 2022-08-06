
# Aluna Diana Faustino de Siqueira
# Exercícios aula 13

# Função para armazenar respostas em uma lista  e retorna as respostas i anexado na lista
def resultados_final(respostas):
    resultados = []
    for i in range(len(respostas)):
        if int(respostas[i]) <= 127:
            resultados.append(i)
    return resultados[0] if len(resultados)==1 else '*'        


while True:
    # Possíveis valores de resposta
    possibilidades = ['A', 'B', 'C', 'D', 'E']
    perguntas = int(input())
    resultados = []
    if not perguntas:
        break
    for i in range(perguntas):
        resultados.append(resultados_final(input().split()))
    # Se a resposta está corretamente marcada, printa qual foi a alternativa selecionada de acordo com 
    # a posição na lista 
    [print(possibilidades[x]) if x != '*' else print('*') for x in resultados]