# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-13 16:22:06
# https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/
# IMPORTANT!! Submit Code Region End(Do not remove this line)
from collections import defaultdict


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        max_s = s = 0
        cnt = defaultdict(int)
        for i, x in enumerate(nums):
            s += x
            cnt[x] += 1

            left = i - k + 1
            if left < 0:
                continue

            if len(cnt) == k:
                max_s = max(max_s, s)

            s -= nums[left]
            cnt[nums[left]] -= 1
            if cnt[nums[left]] == 0:
                del cnt[nums[left]]

        return max_s

# IMPORTANT!! Submit Code Region End(Do not remove this line)
