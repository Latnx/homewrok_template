class Fibonacci:
    n_dac = 0
    n_dp = 0

    def DAC_F(self, n):
        if n == 1 or n == 2:
            return 1
        else:
            self.n_dac += 1
            return self.DAC_F(n - 1) + self.DAC_F(n - 2)

    def DP_F(self, n):
        f = [x for x in range(n + 1)]
        for i in range(1, n + 1):
            if (i == 1) or i == 2:
                f[i] = 1
            else:
                self.n_dp += 1
                f[i] = f[i - 1] + f[i - 2]
        return f[n]
