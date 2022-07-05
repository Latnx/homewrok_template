import random
import matplotlib.pyplot as plt
from Knapsack_DP import Knapsack
import time


def random_list(n):
    list = []
    for i in range(n):
        list.append((random.randint(1, n), random.randint(1, n)))
    return list


n1 = []
n2 = []
n3 = []
n4 = []
n = [n1, n2, n3, n4]
f = open("./data.txt", "w", encoding="utf-8")
for i in range(2000):
    arr = random_list(i)
    a = Knapsack()
    m = [100, 400, 800, 2000]
    for C in range(4):
        old_time1 = time.time()
        a.Knapsack_dp(arr, m[C])
        current_time = time.time()

        n[C].append((current_time - old_time1) * 1000)
        print(a.sum)
    f.write(f"物品[价格][质量]:{arr}\n")
    print(i)

plt.plot(range(2000), n1, label="C=200")
plt.plot(range(2000), n2, label="C=400")
plt.plot(range(2000), n3, label="C=800")
plt.plot(range(2000), n4, label="C=2000")
plt.legend()
plt.show()

plt.savefig("结果.png")
