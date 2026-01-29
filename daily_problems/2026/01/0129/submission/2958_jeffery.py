# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-29 16:39:17
# https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/
# IMPORTANT!! Submit Code Region End(Do not remove this line)
from collections import defaultdict


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for i, x in enumerate(nums):
            cnt[x] += 1
            while cnt[x] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(i - left + 1, ans)
        return ans

# IMPORTANT!! Submit Code Region End(Do not remove this line)
