import random
from datetime import datetime
import os

def partitionLast1(input_list, low, high):
    i = (low - 1)
    pivot = input_list[high]
    for j in range(low, high):
        if input_list[j] <= pivot:
            i = i + 1
            input_list[i], input_list[j] = input_list[j], input_list[i]
    input_list[i + 1], input_list[high] = input_list[high], input_list[i + 1]
    return (i + 1)


def quickSortLast1(input_list, low, high):
    if low < high:
        partition_index = partitionLast1(input_list, low, high)
        quickSortLast1(input_list, low, partition_index - 1)
        quickSortLast1(input_list, partition_index + 1, high)



# srodkowy pivot

def partitionMid1(input_list, low, high):
    input_list[low], input_list[(low + high) // 2] = input_list[(low + high) // 2], input_list[low]
    pivot = input_list[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if input_list[j] < pivot:
            input_list[j], input_list[i] = input_list[i], input_list[j]
            i += 1
    input_list[i - 1], input_list[low] = input_list[low], input_list[i - 1]
    return i - 1


def quickSortMid1(input_list, low, high):
    if low < high:
        pivot = partitionMid1(input_list, low, high)
        quickSortMid1(input_list, low, pivot - 1)
        quickSortMid1(input_list, pivot + 1, high)


def partitionMid2(input_list, low, high):
    input_list[low], input_list[(low + high) // 2] = input_list[(low + high) // 2], input_list[low]
    pivot = input_list[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if input_list[j] > pivot:
            input_list[j], input_list[i] = input_list[i], input_list[j]
            i += 1
    input_list[i - 1], input_list[low] = input_list[low], input_list[i - 1]
    return i - 1


def quickSortMid2(input_list, low, high):
    if low < high:
        pivot = partitionMid2(input_list, low, high)
        quickSortMid2(input_list, low, pivot - 1)
        quickSortMid2(input_list, pivot + 1, high)


# losowy pivot

def partitionRand1(input_list, low, high):
    losliczba = random.randint(low, high)
    input_list[low], input_list[losliczba] = input_list[losliczba], input_list[low]
    pivot = input_list[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if input_list[j] > pivot:
            input_list[j], input_list[i] = input_list[i], input_list[j]
            i += 1
    input_list[i - 1], input_list[low] = input_list[low], input_list[i - 1]
    return i - 1


def quickSortRand1(input_list, low, high):
    if low < high:
        pivot = partitionRand1(input_list, low, high)
        quickSortRand1(input_list, low, pivot - 1)
        quickSortRand1(input_list, pivot + 1, high)


def partitionRand2(input_list, low, high):
    losliczba = random.randint(low, high)
    input_list[low], input_list[losliczba] = input_list[losliczba], input_list[low]
    pivot = input_list[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if input_list[j] < pivot:
            input_list[j], input_list[i] = input_list[i], input_list[j]
            i += 1
    input_list[i - 1], input_list[low] = input_list[low], input_list[i - 1]
    return i - 1


def quickSortRand2(input_list, low, high):
    if low < high:
        pivot = partitionRand2(input_list, low, high)
        quickSortRand2(input_list, low, pivot - 1)
        quickSortRand2(input_list, pivot + 1, high)


def heapify(tablica, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and tablica[largest] < tablica[l]:
        largest = l

    if r < n and tablica[largest] < tablica[r]:
        largest = r

    if largest != i:
        tablica[i], tablica[largest] = tablica[largest], tablica[i]

        heapify(tablica, n, largest)


def heapSort(tablica):
    n = len(tablica)

    for i in range(n // 2 - 1, -1, -1):
        heapify(tablica, n, i)

    for i in range(n - 1, 0, -1):
        tablica[i], tablica[0] = tablica[0], tablica[i]
        heapify(tablica, i, 0)


def heapif2(tablica, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and tablica[l] < tablica[smallest]:
        smallest = l

    if r < n and tablica[r] < tablica[smallest]:
        smallest = r

    if smallest != i:
        (tablica[i],
         tablica[smallest]) = (tablica[smallest],
                           tablica[i])

        heapif2(tablica, n, smallest)


def heapSort2(tablica, n):
    for i in range(int(n / 2) - 1, -1, -1):
        heapif2(tablica, n, i)

    for i in range(n - 1, -1, -1):
        tablica[0], tablica[i] = tablica[i], tablica[0]

        heapif2(tablica, i, 0)


def mergeSort1(tablica3):
    if len(tablica3) > 1:

        srodkowy = len(tablica3) // 2

        L = tablica3[:srodkowy]

        R = tablica3[srodkowy:]

        mergeSort1(L)

        mergeSort1(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tablica3[k] = L[i]
                i += 1
            else:
                tablica3[k] = R[j]
                j += 1
            k += 1

        # Sprawdzanie czy na lewo
        while i < len(L):
            tablica3[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tablica3[k] = R[j]
            j += 1
            k += 1


def mergeSort2(tablica3):
    if len(tablica3) > 1:

        srodkowy = len(tablica3) // 2

        L = tablica3[:srodkowy]

        R = tablica3[srodkowy:]

        mergeSort2(L)

        mergeSort2(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                tablica3[k] = L[i]
                i += 1
            else:
                tablica3[k] = R[j]
                j += 1
            k += 1

        # Sprawdzanie czy element na prawo
        while i < len(L):
            tablica3[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tablica3[k] = R[j]
            j += 1
            k += 1

#200 000 = 1s
#2 500 000
#5kk
#7,5kk
#10kk = 4m i 03s
rozmiartab  = 10000000
print('ilość liczb w tablicy: '+str(rozmiartab)+ ' elementów\n')
for p in range(5):
    tablica = [random.randint(-10000, 10000) for i in range(rozmiartab)]
    tablica1 = list(tablica)    #QuickSort pivot jako ostatni
    tablica2 = list(tablica)    #QuickSort pivot jako środek
    tablica3 = list(tablica)    #QuickSort pivot losowy
    tablica4 = list(tablica)    #HeapSort
    tablica5 = list(tablica)    #MergeSort
    dl = len(tablica)
    n = len(tablica)
    print("\n")
     print("Quick Sort pivot na końcu")
            
     print("Losowe dane")
    t1 = datetime.now()
    quickSortLast1(tablica1, 0, dl - 1)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)
            
    print("Posortowane dane")
    t1 = datetime.now()
    quickSortLast1(tablica1, 0, dl - 1)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)
            
    print("Odwrotne dane")
    t1 = datetime.now()
    quickSortMid1(tablica2, 0, dl - 1)
    t2 = datetime.now()
    t3 = t2 - t1
    t1 = datetime.now()
    print(t3)
    print("\n")
    
    print("Quick Sort pivot na środku")

    print("Losowe dane")
    t1 = datetime.now()
    quickSortMid1(tablica2, 0, dl - 1)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)

    print("Posortowane dane")
    t1 = datetime.now()
    quickSortMid2(tablica2, 0, dl - 1)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)

    print("Odwrotne dane")
    t1 = datetime.now()
    quickSortRand1(tablica3, 0, dl - 1)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)
    print("\n")

    print("Quick Sort pivot losowy")

    print("Losowe dane")
    t1 = datetime.now()
    quickSortRand1(tablica3, 0, dl - 1)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)

    print("Posortowane dane")
    t1 = datetime.now()
    quickSortRand1(tablica3, 0, dl - 1)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)

    print("Odwrotne dane")
    t1 = datetime.now()
    quickSortRand2(tablica3, 0, dl - 1)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)
    print("\n")

    print("Heapsort")

    print("Losowe dane")
    t1 = datetime.now()
    heapSort(tablica4)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)

    print("Posortowane dane")
    t1 = datetime.now()
    heapSort(tablica4)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)

    print("Odwrotne dane")
    t1 = datetime.now()
    heapSort2(tablica4, n)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)
    print("\n")

    print("Merge sort")

    print("Losowe dane")
    t1 = datetime.now()
    mergeSort1(tablica5)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)

    print("Posortowane dane")
    t1 = datetime.now()
    mergeSort1(tablica5)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)

    print("Odwrotne dane")
    t1 = datetime.now()
    mergeSort2(tablica5)
    t2 = datetime.now()
    t3 = t2 - t1
    print(t3)

os.system("PAUSE")