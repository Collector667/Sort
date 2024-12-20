import random
from random import shuffle
import statistics
from numpy.ma.testutils import approx
from selectionSort import *
from insertionSort import *
from bubbleSort import *
from quickSort import *
from mergeSort import *
from shellSort import *
from heapSort import *
import math
import time

x = 0
n = 100000
arr = []
for i in range(n):
    arr.append(random.randint(1, 10000))

times = []
sorttimes = []
resorttimes = []
nedosorttimes = []
n = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000]
for j in n:
    arr = []
    for k in range(j):
        arr.append(random.randint(1, 10000))
    t_s0 = time.time()
    mergeSort(arr)
    t_e0 = time.time()
    times.append(round(t_e0-t_s0, 5))


print(times)







