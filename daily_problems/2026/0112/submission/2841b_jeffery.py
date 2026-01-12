# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-12 14:55:40
# https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/
# IMPORTANT!! Submit Code Region End(Do not remove this line)
from collections import defaultdict


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        for i, x in enumerate(nums):
            s += x
            cnt[x] += 1

            left = i - k + 1
            if left < 0:
                continue

            # 更新答案
            if len(cnt) >= m:
                ans = max(ans, s)

            s -= nums[left]
            cnt[nums[left]] -= 1
            if cnt[nums[left]] == 0:
                del cnt[nums[left]]

        return ans

# IMPORTANT!! Submit Code Region End(Do not remove this line)
