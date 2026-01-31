# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-31 23:30:47
# https://leetcode.cn/problems/max-consecutive-ones-iii/
# IMPORTANT!! Submit Code Region End(Do not remove this line)


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        cnt0 = 0
        left = ans = 0
        for i, x in enumerate(nums):
            cnt0 += 1 - x
            while cnt0 > k:
                cnt0 -= 1 - nums[left]
                left += 1
            ans = max(ans, i - left + 1)
        return ans

    # IMPORTANT!! Submit Code Region End(Do not remove this line)
