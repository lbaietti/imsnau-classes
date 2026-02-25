# Este algoritmo também é baseado na técnica de dividir para conquistar

# Dividir:
# Parte a lista em duas sub-listas, utilizando o algoritmo partition

# Conquistar:
# Ordena as sublistas

# Combinar (merge): 
# Neste algoritmo este passo não é necessário dadas as 
#características do algoritmo partition

# Esquemas de particição de Hoare e Lomuto
# O esquema de partição de Hoare na prática é mais eficiente

# Independentemente do esquema, quando o algoritmo de partição
#  termina, existe a garantia de que: 

# o elemento escolhido para pivot fica na sua posição final, 
# relativamente à ordenação;

# e a sublista do lado direito do pivot tem os elementos
# maiores ou iguais ao pivot.

# ======================================================

# Partition com o esquema de Hoare

# Enquanto os índices i e j não se cruzarem, 
# incrementamos o índice i, até encontrar um elemento 
# maior ou igual ao pivot.

def partition(list, left, right):
    pivot = list[right]
    i = left - 1
    j = right
    while(True):
        i += 1
        while (list[i] < pivot):
            i += 1
        j -= 1
        while(list[j] > pivot):
            j -= 1 
        if(j == left):
            break
        if(i >= j):
            break
        list[i], list[j] = list[j], list[i]
    list[i], list[right] = list[right], list[i]
    return i

# Quick Sort

#Divisão: 

#def quickSort(list, left, right):
 #   if left < right: 
# ->->-> pivot = partition(list, left, right)
   #     quickSort(list, left, pivot - 1)
    #    quickSort(list, pivot + 1, right)

# Conquista:


#def quickSort(list, left, right):
 #   if left < right: 
        #pivot = partition(list, left, right)
# ->->-> quickSort(list, left, pivot - 1)
# ->->-> quickSort(list, pivot + 1, right)

def quickSort(list, left, right):
    if left < right: 
        pivot = partition(list, left, right)
        quickSort(list, left, pivot - 1)
        quickSort(list, pivot + 1, right)