# https://www.algospot.com/judge/problem/read/JLIS
# 파이썬3로 푼사람은 단 한명도 없다.

class Solution:
    def __init__(self, a, b):
        self.n = len(a)
        self.m = len(b)
        self.a = a
        self.b = b
        self.cache = [[-1 for _ in range(self.m + 1)] for __ in range(self.n + 1)]

    def solve(self, index_a, index_b):
        if self.cache[index_a + 1][index_b + 1] != -1:
            return self.cache[index_a + 1][index_b + 1]

        a_num = self.a[index_a] if index_a != -1 else float('-inf')
        b_num = self.b[index_b] if index_b != -1 else float('-inf')
        num = max(a_num, b_num)

        self.cache[index_a + 1][index_b + 1] = 2
        for i in range(index_a + 1, self.n):
            if self.a[i] > num:
                self.cache[index_a + 1][index_b + 1] = max(self.cache[index_a + 1][index_b + 1],
                                                           self.solve(i, index_b) + 1)
        for i in range(index_b + 1, self.m):
            if self.b[i] > num:
                self.cache[index_a + 1][index_b + 1] = max(self.cache[index_a + 1][index_b + 1],
                                                           self.solve(index_a, i) + 1)
        return self.cache[index_a + 1][index_b + 1]


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        n, m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        solution = Solution(a, b)
        print(solution.solve(-1, -1) - 2)
