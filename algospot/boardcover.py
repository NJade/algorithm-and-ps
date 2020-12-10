# https://www.algospot.com/judge/problem/read/BOARDCOVER

class Solution:
    def __init__(self, board, H, W):
        self.covers = [
            [[0, 0], [0, 1], [1, 1]],
            [[0, 0], [0, 1], [1, 0]],
            [[0, 0], [1, 0], [1, 1]],
            [[0, 0], [1, 0], [1, -1]]
        ]
        self.H = H
        self.W = W
        self.board = board

    def solve(self):
        first_y = -1
        first_x = -1
        for y in range(H):
            for x in range(W):
                if self.board[y][x] == 0:
                    first_x = x
                    first_y = y
                    break
            if first_y != -1:
                break
        if first_y == -1:
            return 1

        ret = 0
        for type in range(4):
            if self.check(first_x, first_y, type):
                self.cover(first_x, first_y, type)
                ret += self.solve()
                self.uncover(first_x, first_y, type)
        return ret

    def cover(self, x, y, type):
        for i in range(3):
            ny = y + self.covers[type][i][0]
            nx = x + self.covers[type][i][1]
            self.board[ny][nx] = 1

    def uncover(self, x, y, type):
        for i in range(3):
            ny = y + self.covers[type][i][0]
            nx = x + self.covers[type][i][1]
            self.board[ny][nx] = 0

    def check(self, x, y, type):
        for i in range(3):
            ny = y + self.covers[type][i][0]
            nx = x + self.covers[type][i][1]
            if not self.is_inside(nx, ny):
                return False
            if self.board[ny][nx] != 0:
                return False
        return True

    def is_inside(self, x, y):
        if y < 0 or y >= self.H or x < 0 or x >= self.W:
            return False
        return True


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        H, W = map(int, input().split())
        board = [[0 for _ in range(W)] for _ in range(H)]

        for y in range(H):
            line = input()
            for x in range(W):
                if line[x] == '#':
                    board[y][x] = 1
                else:
                    board[y][x] = 0

        solution = Solution(board, H, W)
        print(solution.solve())
