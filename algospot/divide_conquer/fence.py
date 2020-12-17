# https://www.algospot.com/judge/problem/read/FENCE
# 클래스나 기타 등등을 하면 시간초과가 된다.
# 시간 초과가 나지 않는 코드를 첨부한다.

class Solution:
    def __init__(self, fence):
        self.fence = fence

    def solve(self, first, last):
        if first == last:
            return self.fence[first]

        mid = first + (last - first) // 2
        left, right = mid, mid + 1
        h = min(self.fence[left], self.fence[right])

        ret = max(self.solve(first, mid), self.solve(mid + 1, last), h * 2)

        while first < left or right < last:
            if right < last and (left == first or self.fence[left - 1] < self.fence[right + 1]):
                right += 1
                h = min(h, self.fence[right])
            else:
                left -= 1
                h = min(h, self.fence[left])
            ret = max(ret, h * (right - left + 1))
        return ret


if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        w = int(input())
        fence = list(map(int, input().split()))
        solution = Solution(fence)
        print(solution.solve(0, w - 1))

# def solve(first, last):
#     if first == last:
#         return fence[first]
#
#     mid = first + (last - first) // 2
#     left, right = mid, mid + 1
#     h = min(fence[left], fence[right])
#
#     ret = max(solve(first, mid), solve(mid + 1, last), h * 2)
#
#     while first < left or right < last:
#         if right < last and (left == first or fence[left - 1] < fence[right + 1]):
#             right += 1
#             h = h if h < fence[right] else fence[right]
#         else:
#             left -= 1
#             h = h if h < fence[left] else fence[left]
#         area = h * (right - left + 1)
#         ret = ret if ret > area else area
#     return ret
#
#
# c = int(input())
# for _ in range(c):
#     w = int(input())
#     fence = list(map(int, input().split()))
#     print(solve(0, w - 1))
