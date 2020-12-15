# https://www.algospot.com/judge/problem/read/CLOCKSYNC
# python 으로는 완전탐색으로 풀리지 않는다.
# 최근에는 이런식으로 언어특성으로 인해 풀리지 않는 경우는 없다.
# 이것은 이렇게 넘어가고 다음에 최적화를 더 살펴보도록 한다.

class Solution:
    def __init__(self, clocks):
        self.switches = [
            [0, 1, 2],
            [3, 7, 9, 11],
            [4, 10, 14, 15],
            [0, 4, 5, 6, 7],
            [6, 7, 8, 10, 12],
            [0, 2, 14, 15],
            [3, 14, 15],
            [4, 5, 7, 14, 15],
            [1, 2, 3, 4, 5],
            [3, 4, 5, 9, 13]
        ]
        self.clocks = clocks

    def solve(self, switch):
        if not any(self.clocks):
            return 0

        if switch == 10:
            return 123456789

        ret = 123456789
        for i in range(4):
            ret = min(ret, i + self.solve(switch + 1))
            self.push(switch)
        return ret

    def push(self, switch):
        for clock in self.switches[switch]:
            self.clocks[clock] = (self.clocks[clock] + 1) % 4


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        clocks = list(map(int, input().split()))
        clocks = [clock // 3 % 4 for clock in clocks]
        solution = Solution(clocks)
        sol = solution.solve(0)
        if sol == 123456789:
            sol = -1
        print(sol)
