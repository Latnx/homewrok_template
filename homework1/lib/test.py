import random
import matplotlib.pyplot as plt

import a
from Bubble import Bubble
from MergeSort import mergeSort
from QuickSort import QuickSort


def random_list(n):
    list = []
    for i in range(n):
        list.append(random.randint(0, n))
    return list


n1 = []
n2 = []
n3 = []
f = open("./data.txt", "w")
for i in range(1000):
    a = QuickSort()
    arr = random_list(i)
    f.write(str(arr)+'\n')
    n1.append(Bubble(arr.copy(), i))
    n2.append(mergeSort(arr.copy(), 0, i - 1))
    n3.append(a.quickSort(arr.copy(), 0, i - 1))
    print(i)

plt.plot(range(1000), n1, label="Bubble")
plt.plot(range(1000), n2, label="MergeSort")
plt.plot(range(1000), n3, label="QuickSort")
plt.legend()
plt.show()
plt.savefig("结果.png")
