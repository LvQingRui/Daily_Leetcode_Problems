# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-22 00:14:06
# https://leetcode.cn/problems/minimum-removals-to-balance-array/
# IMPORTANT!! Submit Code Region End(Do not remove this line)


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        nums.sort()
        max_s = left = 0
        for right, x in enumerate(nums):
            while nums[left] * k < x:
                left += 1
            max_s = max(max_s, right - left + 1)
        return len(nums) - max_s
# IMPORTANT!! Submit Code Region End(Do not remove this line)
