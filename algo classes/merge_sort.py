# O desenho e a análise de algoritmos são fundamentais na programação e na Engenharia de Software.
#  A escolha dos algoritmos e das estruturas de dados mais indicadas, são essenciais 
#para construir software eficiente e escalável

# MergeSort -> Técnica Dividir para conquistar

# Dividir o problema e sub-problema: 
# -> Instâncias menores no mesmo problema 

# Conquistar os sub-problemas: 
# -> Resolvendo-os recursivamente

# Combinar as soluções dos sub-problemas:
# -> Para obter a solução do problema inicial

# Divisão: 
# Divide a lista list em duas sub-listas de tamanho idêntico

#def mergesort(list):
    #if len(list) <= 1:
     #   return list
    #mid - len(list) // 2
    #leftHalf = ->->-> mergesort(arr[:mid+1]) <-<-<-
    #rightHalf = ->->-> mergesort(arr[mid+1:]) <-<-<-
    # return merge(leftHalf, rightHalf)

# Conquista: 
# ordena as duas sub-listas com as chamadas recursivas

#def mergesort(list):
    #if len(list) <= 1:
     #   return list
    #mid - len(list) // 2
    # ->->-> leftHalf = mergesort(arr[:mid+1]) 
    # ->->-> rightHalf = mergesort(arr[mid+1:]) 
    # return merge(leftHalf, rightHalf)

# Combina:
# Junta de forma ordenada (função merge) as sub-listas na lista list.
# Note-se que as sub-lists já estão ordenadas

#def mergesort(list):
    #if len(list) <= 1:
     #   return list
    #mid - len(list) // 2
    #leftHalf = mergesort(arr[:mid+1]) 
    #rightHalf = mergesort(arr[mid+1:]) 
    # return ->->-> merge(leftHalf, rightHalf)

#===============================================

def mergesort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftHalf = mergesort(arr[:mid+1]) 
    rightHalf = mergesort(arr[mid+1:]) 
    return merge(leftHalf, rightHalf)

# Sejam leftHalf e rightHalf duas listas ordenadas de modo crescente

def merge(leftHalf, rightHalf):
    result = []
    i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if left[i] <= right[j]:
            result.append(leftHalf[i])
            i += 1
        else:
            result.append(rightHalf[j])
            j += 1
    result.extend(leftHalf[i:])
    result.extend(rightHalf[j:])
    return result

# Esta operação, devolve uma nova lista, também ordenada com tdos os elementos nas listas dadas de entrada

#================================================

# Implementação alternativa 

def mergesort(arr, left, right):
    if left < right:
        mid = (left + right) //2
        mergesort(arr, left, mid)
        mergesort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else: 
            arr[k] = L[i]
            j += 1
        k += 1

    while i < n1: 
        arr[k] = L[i]
        i += 1
        k += 1 

    while j < n2: 
        arr[k] = R[j]
        j += 1 
        k += 1 