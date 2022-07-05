class Knapsack:
    sum = 0

    def Knapsack_dp(self, v_m, C):
        n = len(v_m)
        m = [[0 for i in range(C + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):  # 个数
            for w in range(1, C + 1):  # 重量
                self.sum += 1
                if (w - v_m[i - 1][1]) < 0:  # 装不进
                    m[i][w] = m[i - 1][w]
                    continue
                m[i][w] = max(
                    m[i - 1][w],
                    m[i - 1][w - v_m[i - 1][1]] + v_m[i - 1][0]
                )  # 比较装还是不装

# a = Knapsack
# a.Knapsack_dp(a, [0, 0], 3)
