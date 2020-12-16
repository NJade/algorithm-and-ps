# https://algospot.com/judge/problem/read/QUADTREE

class Solution:
    def __init__(self, quad):
        self.quad = quad

    def solve(self):
        head = self.quad[0]
        self.quad = self.quad[1:]
        if head == 'b' or head == 'w':
            return head
        upper_left = self.solve()
        upper_right = self.solve()
        lower_left = self.solve()
        lower_right = self.solve()
        return 'x' + lower_left + lower_right + upper_left + upper_right


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        quad = input()
        solution = Solution(quad)
        print(solution.solve())
