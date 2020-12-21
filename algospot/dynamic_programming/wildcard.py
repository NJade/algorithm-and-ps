import sys

sys.setrecursionlimit(150000)


class Solution:
    def __init__(self, w, s):
        self.cache = [[-1 for _ in range(101)] for _ in range(101)]
        self.w = w
        self.s = s

    def solve(self, w_pos, s_pos):
        if self.cache[w_pos][s_pos] != -1:
            return self.cache[w_pos][s_pos]

        cache_w_pos = w_pos
        cache_s_pos = s_pos

        while s_pos < len(self.s) and w_pos < len(self.w) and (self.s[s_pos] == self.w[w_pos] or self.w[w_pos] == '?'):
            self.cache[w_pos][s_pos] = self.solve(w_pos + 1, s_pos + 1)
            return self.cache[w_pos][s_pos]

        if w_pos == len(self.w):
            if s_pos == len(self.s):
                self.cache[cache_w_pos][cache_s_pos] = 1
            else:
                self.cache[cache_w_pos][cache_s_pos] = 0
            return self.cache[cache_w_pos][cache_s_pos]

        if self.w[w_pos] == '*':
            if self.solve(w_pos + 1, s_pos) == 1 or (s_pos < len(self.s) and self.solve(w_pos, s_pos + 1)):
                self.cache[cache_w_pos][cache_s_pos] = 1
                return 1
        self.cache[cache_w_pos][cache_s_pos] = 0
        return 0


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        w = input()
        n = int(input())
        l = []
        for _ in range(n):
            s = input()
            solution = Solution(w, s)
            if solution.solve(0, 0) == 1:
                l.append(s)
        l.sort()
        for t in l:
            print(t)
