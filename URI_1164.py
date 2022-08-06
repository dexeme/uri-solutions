
# Aluna Diana Faustino de Siqueira
# Exercícios aula 13

contador = 0
n = int(input())
# Caso não esteja na faixa de valores aceita
if not 1 <= n <= 10**8:
    print('Insira um número entre 1 e 10^8')
else:
    # Vai do divisor 1 até o número n-1 (já que não podemos incluir ele mesmo)
    for i in range (1, n-1):
        # Se o número dividido por esse número der divisão exata, então soma o número no contador
        if n % i == 0:
            contador += i

    # Agora, se o contador (soma dos números do intervalo na condição)
    # For exatamente igual ao n inicial, então ele é perfeito
    if contador == n:
        print('eh perfeito')
    else:
        print('nao eh perfeito')
