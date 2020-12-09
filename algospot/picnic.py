# https://www.algospot.com/judge/problem/read/PICNIC

class Solution:
    def __init__(self, n):
        self.friends = [[False for _ in range(n)] for _ in range(n)]
        self.pairings = [False for _ in range(n)]

    def set_friends(self, i, j):
        self.friends[i][j] = True
        self.friends[j][i] = True

    def count_pair_recursion(self):
        first_find_not_pair = -1
        ret = 0
        for i in range(n):
            if not self.pairings[i]:
                first_find_not_pair = i
                break

        if first_find_not_pair == -1:
            return 1

        for i in range(first_find_not_pair + 1, n):
            if not self.pairings[i] and self.friends[first_find_not_pair][i]:
                self.pairings[first_find_not_pair] = True
                self.pairings[i] = True
                ret += self.count_pair_recursion()
                self.pairings[first_find_not_pair] = False
                self.pairings[i] = False
        return ret


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        n, m = map(int, input().split())
        solution = Solution(n)
        t = list(map(int, input().split()))
        for i in range(0, len(t), 2):
            solution.set_friends(t[i], t[i + 1])
        print(solution.count_pair_recursion())
