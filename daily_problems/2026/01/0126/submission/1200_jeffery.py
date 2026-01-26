# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-26 23:00:03
# https://leetcode.cn/problems/minimum-absolute-difference/
# IMPORTANT!! Submit Code Region End(Do not remove this line)
import math


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        min_diff = math.inf
        ans = []
        for x, y in pairwise(arr):
            diff = y - x
            if diff < min_diff:
                min_diff = diff
                ans = [[x, y]]
            elif diff == min_diff:
                ans.append([x, y])
        return ans
# IMPORTANT!! Submit Code Region End(Do not remove this line)
