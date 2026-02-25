#Bubble Sort 
# Dados de entrada: Lista de n elementos
# Ordenação de modo crescente

#lista | 10 | 8 | 15 | 5 | 6 |
        # 0   1   2    3   4

#1ª Passagem 
# lista | 10 | 8 | 15 | 5 | 6 |
        # 0   1   2    3   4

#| 8 | 10 | 15 | 5 | 6 |    10 < 15 então não troca 
#  0   1   2    3   4

#| 8 | 10 | 5 | 15 | 6 |   15 > 5 então troca
#  0   1   2    3   4

#| 8 | 10 | 5 | 6 | 15 |
#  0   1   2    3   4


#2ª Passagem 
# lista | 8 | 10 | 5 | 6 | 15 |
        # 0   1   2    3   4

#| 8 | 10 | 5 | 6 | 15 |    8 < 10 então não troca 
#  0   1   2    3   4

#| 8 | 5 | 10 | 6 | 15 |   10 > 5 então troca
#  0   1   2    3   4

#| 8 | 5 | 6 | 10 | 15 | 10 > 6 então troca
#  0   1   2    3   4

#3ª Passagem 
# lista | 8 | 5 | 6 | 10 | 15 |
        # 0   1   2    3   4

#| 5 | 8 | 6 | 10 | 15 |    5 < 8 então não troca 
#  0   1   2    3   4

#| 5 | 6 | 8 | 10 | 15 |   8 > 6 então troca
#  0   1   2    3   4


#4ª Passagem 
# lista | 5 | 6 | 8 | 10 | 15 |
        # 0   1   2    3   4

# Se não houver nenhuma otimização no algoritmo, teria que comparar os 2 primeiros  confirmar que ambos estão na ordem correta

def bubbleSort(list):
    n = len(list)
    for i in range (n):
        for j in range (0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

#Complexidade em termos de tempo
# -> Com otimização: melhor caso: Omega de N; Pior caso: O de n ao quadrado
# -> Sem otimização: Theta de n ao quadrado              

