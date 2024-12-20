def selectionSort(mas):
    n = len(mas)
    for i in range(n):
        j = i
        for k in range(i+1, n):
            if (mas[j] > mas[k]):
                j = k
        mas[j], mas[i] = mas[i], mas[j]

