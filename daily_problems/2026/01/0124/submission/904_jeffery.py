# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-24 23:43:35
# https://leetcode.cn/problems/fruit-into-baskets/
# IMPORTANT!! Submit Code Region End(Do not remove this line)
from collections import defaultdict


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right, in_ in enumerate(fruits):
            cnt[in_] += 1  # fruits[right] 进入窗口
            while len(cnt) > 2:  # 不满足要求
                out = fruits[left]
                cnt[out] -= 1  # fruits[left] 离开窗口
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# IMPORTANT!! Submit Code Region End(Do not remove this line)
