# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-15 15:55:23
# https://leetcode.cn/problems/minimum-size-subarray-sum/
# IMPORTANT!! Submit Code Region End(Do not remove this line)


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        ans = n + 1  # 或者是 math.inf
        left = 0  # 左端点
        s = 0

        for right, x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans <= n else 0

# IMPORTANT!! Submit Code Region End(Do not remove this line)
