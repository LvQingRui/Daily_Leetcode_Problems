# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-25 23:54:06
# https://leetcode.cn/problems/minimum-prefix-removal-to-make-array-strictly-increasing/
# IMPORTANT!! Submit Code Region End(Do not remove this line)


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)
        start = n - 1  # 至少最后一个元素的后缀一定严格递增
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                start = i
            else:
                break
        return start
# IMPORTANT!! Submit Code Region End(Do not remove this line)
