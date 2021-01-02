# https://www.algospot.com/judge/problem/read/PI
# 시간초과가 발생한다.
# 정답을 맞춘 사람들을 보면 list slicing을 하지 않고 함수 인자로 직접 다 던지는 등의 시도를 한다.
# 플랫폼의 문제로 넘어간다.
import sys

sys.setrecursionlimit(1000 * 1000)


class Solution:
    def __init__(self, n):
        self.n = n
        self.cache = [-1 for _ in range(len(self.n))]

    def solve(self, start):
        if start == len(self.n):
            return 0
        if self.cache[start] != -1:
            return self.cache[start]
        self.cache[start] = 123456789
        for i in range(3, 6):
            if start + i <= len(self.n):
                temp = self.solve(start + i) + self.classify(start, start + i - 1)
                self.cache[start] = min(self.cache[start], temp)
        return self.cache[start]

    def classify(self, start, end):
        temp = self.n[start:end + 1]
        if temp == (temp[0] * len(temp)):
            return 1
        progression = True
        for i in range(len(temp) - 1):
            if temp[i + 1] - temp[i] != temp[1] - temp[0]:
                progression = False
        if progression and abs(temp[1] - temp[0]) == 1:
            return 2
        repeat = True
        for i in range(len(temp)):
            if temp[i] != temp[i % 2]:
                repeat = False
        if repeat:
            return 4
        if progression:
            return 5
        return 10


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        n = list(map(int, input().strip()))
        solution = Solution(n)
        print(solution.solve(0))
