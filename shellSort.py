import math
def pratgaps(arr):
    gaps=[]
    n = len(arr)
    for i in range(round(math.log2(n))):
        for j in range(round(math.log2(n)//2)):
            if ((2**i)*(3**j)) <= n/2:
                temp = (2**i)*(3**j)
                gaps.append((2**i)*(3**j))

    gaps.sort(reverse = True)
    return gaps

def shellgaps(arr):
    gaps= []
    n = len(arr)
    while n > 1:
        gaps.append(n//2)
        n = n//2
    return gaps

def hibbardgaps(arr):
    gaps = []
    n = len(arr)
    i = math.floor(math.log2(n/2))
    for k in range(i, 0, -1):
        gaps.append(2**k-1)
    return gaps

def shellSort(mas, gaps):
    n = len(mas)
    for gap in gaps:
        for i in range(gap, n):
            j = i
            temp = mas[i]

            while((j >= gap) and (mas[j-gap] > temp)):
                mas[j] = mas[j-gap]
                j = j - gap
            mas[j] = temp

