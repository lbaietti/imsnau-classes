# Heap Sprt é um algoritmo de ordenação baseado em comparação 
# que utiliza a estrutura de dados de heap para ordenar os elementos. 
# O algoritmo é eficiente e tem uma complexidade de tempo de O(n log n) no pior caso, 
# o que o torna uma escolha popular para ordenar grandes conjuntos de dados.

# Com o Heap Sort, os elementos são organizados em uma estrutura de dados de heap,
# que é uma árvore binária completa onde cada nó é maior (no caso de um max heap) 
# ou menor (no caso de um min heap) do que seus filhos. 
# O algoritmo começa construindo um max heap a partir dos elementos da lista, 
# e em seguida, o maior elemento (a raiz do heap) é removido e colocado no final da lista. 
# O processo é repetido para os elementos restantes, reconstruindo o heap a cada remoção, até que
# todos os elementos estejam ordenados.

# Max Heap

def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2    

# Algoritmo Fix Down

fixDown(arr, 1, 10)

def exchage(arr, i, j):
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def fix_down(arr, i, size):
    l = left(i)
    r = right(i)
    largest = i

    if (l < size and arr[l] > arr[largest]):
        largest = l
    if (r < size and arr[r] > arr[largest]):
        largest = r
    if (largest != i):
        exchage(arr, i, largest)
        fixDown(arr, largest, size)


# Construir o Max Heap

def buildHeap(arr):
    for i in range(parent(len(arr) - 1), -1, -1):
        fixDown(arr, i, len(arr))  

# Heap Sort
def heapSort(list):
    n = len(list)
    buildHeap(list)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):

        # Move root to end
        list[0], list[i] = list[i], list[0]

        # call max heapify on the reduced heap
        fixDown(list, 0, i)









