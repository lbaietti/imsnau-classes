#Dados de entrada: Lista de n elementos
#Ordenação de modo crescente 
# lista | 10 | 8 | 15 | 5 | 6 |
        # 0    1   2    3   4

# Passo 1: Selecionar o 1º menor elemento (i=0)
# lista | 10 | 8 | 15 | 5 | 6 |
        # 0    1   2    3   4

        #| 5 | 8 | 15 | 10 | 6 |    Troca de elementos
        # 0    1   2    3   4

# Passo 2: Selecionar o 2º menor elemento (i=0)
# lista | 5 | 8 | 15 | 10 | 6 |
        # 0    1   2    3   4

        #| 5 | 6 | 15 | 10 | 8 |    Troca de elementos
        # 0    1   2    3   4


# Passo 3: Selecionar o 3º menor elemento (i=0)
# lista | 5 | 6 | 15 | 10 | 8 |
        # 0    1   2    3   4

        #| 5 | 6 | 8 | 10 | 15 |    Troca de elementos
        # 0    1   2    3   4


# Passo 4: Selecionar o 4º menor elemento (i=0)
# lista | 5 | 6 | 8 | 10 | 15 |
        # 0    1   2    3   4

        #| 5 | 6 | 8 | 10 | 15 |    Verificado que a lista ficou ordenada de modo crescente
        # 0    1   2    3   4

def selectionSort(list):
    n = len(list) #cumprimento da lista
    for i in range (0, n-1): # Lista começa em 0 e finaliza em n-1
        idxMin = i #Index Min i
        for j in range (i+1, n):
            if list[j] < list[idxMin]:
                idxMin = j
        list[i], list[idxMin] = list[idxMin], list[i]

