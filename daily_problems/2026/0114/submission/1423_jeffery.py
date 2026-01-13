# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-14 00:33:53
# https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/
# IMPORTANT!! Submit Code Region End(Do not remove this line)
import math


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        min_s = math.inf
        s = 0
        n = len(cardPoints)
        m = n - k
        for i, x in enumerate(cardPoints):
            s += x

            left = i - m + 1

            if m == 0:
                return sum(cardPoints)

            if left < 0:
                continue
            min_s = min(s, min_s)

            s -= cardPoints[left]
        return sum(cardPoints) - min_s

# IMPORTANT!! Submit Code Region End(Do not remove this line)
