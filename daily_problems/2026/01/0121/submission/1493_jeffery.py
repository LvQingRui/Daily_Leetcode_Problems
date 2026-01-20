# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-21 00:26:51
# https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/
# IMPORTANT!! Submit Code Region End(Do not remove this line)


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        cnt0 = 0
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            cnt0 += 1 - x
            # if x == 0:
            #     cnt0 += 1
            while cnt0 > 1:
                cnt0 -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left)
        return ans
# IMPORTANT!! Submit Code Region End(Do not remove this line)
