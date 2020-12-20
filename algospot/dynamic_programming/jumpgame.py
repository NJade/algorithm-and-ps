# https://www.algospot.com/judge/problem/read/JUMPGAME

class Solution:
    def __init__(self, n, board):
        self.n = n
        self.board = board
        self.cache = [[-1 for _ in range(n)] for _ in range(n)]

    def solve(self, y, x):
        if y >= self.n or x >= self.n:
            return 0
        if y == (self.n - 1) and x == (self.n - 1):
            return 1

        if self.cache[y][x] != -1:
            return self.cache[y][x]

        sz = self.board[y][x]
        self.cache[y][x] = (self.solve(y + sz, x) or self.solve(y, x + sz))
        return self.cache[y][x]


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        n = int(input())
        board = [[] for _ in range(n)]
        for i in range(n):
            board[i] = list(map(int, input().split()))
        solution = Solution(n, board)
        ret = solution.solve(0, 0)
        if ret == 1:
            print("YES")
        else:
            print("NO")
