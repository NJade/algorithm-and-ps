# https://www.algospot.com/judge/problem/read/LIS

class Solution:
    def __init__(self, l):
        self.l = l
        self.n = len(l)
        self.cache = [-1 for _ in range(self.n)]

    def solve(self, start):
        if self.cache[start] != -1:
            return self.cache[start]

        self.cache[start] = 1
        for i in range(start + 1, self.n):
            if self.l[start] < self.l[i]:
                self.cache[start] = max(self.cache[start], self.solve(i) + 1)
        return self.cache[start]


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        n = int(input())
        l = list(map(int, input().split()))
        solution = Solution(l)
        ret = 0
        for i in range(n):
            ret = max(ret, solution.solve(i))
        print(ret)
