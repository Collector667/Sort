import sys
sys.setrecursionlimit(2000000000)
def merge(a, b):
    mas = []
    i_a, i_b = 0, 0
    len_a, len_b = len(a), len(b)
    while i_a < len_a and i_b < len_b:
        if a[i_a] <= b[i_b]:
            mas.append(a[i_a])
            i_a += 1
        else:
            mas.append(b[i_b])
            i_b += 1
    mas += a[i_a:] + b[i_b:]
    return mas

def mergeSort(mas):
    if len(mas) <= 1:
        return mas
    return merge(mergeSort(mas[:len(mas) // 2]), mergeSort(mas[len(mas) // 2:]))