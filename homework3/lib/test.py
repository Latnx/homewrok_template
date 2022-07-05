import random
import matplotlib.pyplot as plt
from Knapsack_Greedy import Knapsack
import time


def random_list(n):
    list = []
    for i in range(n):
        list.append((random.randint(1, n), random.randint(1, n)))
    return list


n1 = []
n2 = []
n3 = []
f = open("./data.txt", "w", encoding="utf-8")
for i in range(2000):
    arr = random_list(i)
    a = Knapsack()
    m = random.randint(0, int(i * i / 2))
    x = [0] * i

    old_time1 = time.time()
    arr.sort(key=lambda x: x[0] / x[1], reverse=True)
    old_time2 = time.time()
    a.KnapsackGreedy(arr, m, x)
    current_time = time.time()

    f.write(f'背包重量:{m}\n')
    f.write(f"物品[价格][质量]:{arr}\n")
    f.write(f"解向量:{x}\n\n")
    print(current_time - old_time1, current_time - old_time2)
    n1.append((current_time - old_time1)*1000)
    n2.append((current_time - old_time2)*1000)
    n3.append(a.n)

plt.plot(range(2000), n1, label="unsorted")
plt.plot(range(2000), n2, label="sorted")
# plt.plot(range(2000), n3, label="n")
plt.legend()
plt.show()
plt.savefig("结果.png")
