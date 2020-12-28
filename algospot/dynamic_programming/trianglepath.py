# https://www.algospot.com/judge/problem/read/TRIANGLEPATH

class Solution:
    def __init__(self, n, tri):
        self.n = n
        self.tri = tri
        self.cache = [[-1 for _ in range(n)] for _ in range(n)]

    def solve(self, y, x):
        if y == self.n - 1:
            return self.tri[y][x]

        if self.cache[y][x] != -1:
            return self.cache[y][x]

        self.cache[y][x] = self.tri[y][x] + max(self.solve(y + 1, x), self.solve(y + 1, x + 1))
        return self.cache[y][x]


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        n = int(input())
        tri = [[] for _ in range(n)]
        for i in range(n):
            tri[i] = list(map(int, input().split()))
        solution = Solution(n, tri)
        print(solution.solve(0, 0))
