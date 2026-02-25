def insertionSort(list):
    n=len(list)
    for i in range(1, n):
        v = list[i]
        j = i-1
        while j >= 0 and v < list[j]:
            list[j+1] = list[j]
            j = j-1
        list[j+1]=v

#The Insertion Sort algorithm works by iterating through
# the list, taking one element at a time and inserting it 
# into its correct position within the already sorted portion
# of the list. 