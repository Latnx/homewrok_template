class Knapsack:
    i = 0
    n = 0

    def KnapsackGreedy(self, v_w, m, x):
        cu = m  # 剩余容量
        val = 0
        for self.i in range(len(x)):
            if v_w[self.i][1] > cu:
                break
            x[self.i] = 1
            cu = cu - v_w[self.i][1]
            val += v_w[self.i][1]
            self.n += 1
        if self.i < len(x):
            x[self.i] = cu / v_w[self.i][1]
