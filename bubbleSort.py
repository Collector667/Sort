def bubbleSort(mas):
    n = len(mas)
    for i in range(n-1):
        flag = 1
        for j in range(n-i-1):
            if mas[j] > mas[j+1]:
                mas[j], mas[j+1] = mas[j+1], mas[j]
                flag = 0
        if flag == 1:
            break
