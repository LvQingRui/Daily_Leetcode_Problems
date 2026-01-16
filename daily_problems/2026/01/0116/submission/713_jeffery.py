# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-16 12:25:15
# https://leetcode.cn/problems/subarray-product-less-than-k/
# IMPORTANT!! Submit Code Region End(Do not remove this line)


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        ans = 0
        left = 0
        prod = 1

        if k <= 1:
            return 0

        for right, x in enumerate(nums):
            prod *= x

            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

# IMPORTANT!! Submit Code Region End(Do not remove this line)
