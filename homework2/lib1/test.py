import random
import matplotlib.pyplot as plt
from Fibonacci import Fibonacci
import time


def random_list(n):
    list = []
    for i in range(n):
        list.append((random.randint(1, n), random.randint(1, n)))
    return list


n1 = []
n2 = []
f = open("./data.txt", "w", encoding="utf-8")
for i in range(1,31):
    a = Fibonacci()
    a.DAC_F(i)
    a.DP_F(i)
    n1.append(a.n_dac)
    n2.append(a.n_dp)
    print(a.n_dac)
    print(a.n_dp)
    print(i)

plt.plot(range(30), n1, label="dac")
plt.plot(range(30), n2, label="dp")
plt.legend()
plt.show()

plt.savefig("结果.png")
