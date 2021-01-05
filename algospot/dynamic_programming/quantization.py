# https://www.algospot.com/judge/problem/read/QUANTIZE

class Solution:
    def __init__(self, l, s):
        self.l = sorted(l)
        self.s = s
        self.n = len(l)
        self.p_sum = [0 for _ in range(self.n)]
        self.p_square_sum = [0 for _ in range(self.n)]
        self.cache = [[-1 for _ in range(s + 1)] for _ in range(self.n)]
        self.preprocessing()

    def preprocessing(self):
        self.p_sum[0] = self.l[0]
        self.p_square_sum[0] = self.l[0] * self.l[0]
        for i in range(1, self.n):
            self.p_sum[i] = self.p_sum[i - 1] + self.l[i]
            self.p_square_sum[i] = self.p_square_sum[i - 1] + self.l[i] * self.l[i]

    def solve(self, start, rest):
        if start == self.n:
            return 0
        if rest == 0:
            return 123456789
        if self.cache[start][rest] != -1:
            return self.cache[start][rest]
        ret = 123456789

        for i in range(1, self.n - start + 1):
            ret = min(ret, self.min_error(start, start + i - 1) + self.solve(start + i, rest - 1))

        self.cache[start][rest] = ret
        return self.cache[start][rest]

    def min_error(self, start, end):
        start_sum = 0 if start == 0 else self.p_sum[start - 1]
        summation = self.p_sum[end] - start_sum
        start_square_sum = 0 if start == 0 else self.p_square_sum[start - 1]
        square_sum = self.p_square_sum[end] - start_square_sum
        m = int(0.5 + summation / (end - start + 1))
        return square_sum - 2 * m * summation + m * m * (end - start + 1)


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        n, s = list(map(int, input().split()))
        l = list(map(int, input().split()))
        solution = Solution(l, s)
        print(solution.solve(0, s))
