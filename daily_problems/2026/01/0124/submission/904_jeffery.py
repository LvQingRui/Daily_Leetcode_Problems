# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-24 23:43:35
# https://leetcode.cn/problems/fruit-into-baskets/
# IMPORTANT!! Submit Code Region End(Do not remove this line)
from collections import defaultdict


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = ans = 0
        cnt = defaultdict(int)
        for right, x in enumerate(fruits):
            cnt[x] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    del cnt[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# IMPORTANT!! Submit Code Region End(Do not remove this line)
