# Insertion, selection, bubble, merge, quick e heap sort
# são algortimos de ordenação baseados em comparação.

# Counting Sort é um dos algoritmos de ordenação em tempo linear
# que utilizam outras técnicas que não as comparações para
# determinar a ordenação dos elementos. 

# A estratégia do Counting Sort é contar o número de 
# ocorrências de cada elemento em um array de entrada,
# e depois usar essa contagem para determinar a posição 
# de cada elemento na saída ordenada. 
# O algoritmo é eficiente para ordenar inteiros em um 
# intervalo limitado, e tem uma complexidade de tempo 
# de O(n + k), onde n é o número de elementos na entrada e
# k é o valor máximo dos elementos a serem ordenados.

# ===========================================================
# Counting Sort
def count_sort(listA):
    # Finding the maximum element of listA
    k = max(listA)

    # Initializing listC with 0: listC[i] will store the count of elements equal to i
    listC = [0] * (k + 1)

    # 1st step
    for num in listA:
        listC[num] += 1

    # 2nd step: C[i] now contains the number of elements less than or equal to i
    for i in range(1, k + 1):
        listC[i] += listC[i - 1]

    # 3rd step: Building the output listB
    listB = [0] * len(listA)

    for i in range(len(listA) - 1, -1, -1):
        listB[listC[listA[i]] - 1] = listA[i]
        listC[listA[i]] -= 1
    return listB