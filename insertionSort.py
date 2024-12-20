def insertionSort(mas):
    n = len(mas)
    for i in range(n):
        j = i
        temp = mas[i]
        while ( (j>0) and (mas[j - 1] > temp)):
            mas[j] = mas[j - 1]
            j = j - 1
        mas[j] = temp
