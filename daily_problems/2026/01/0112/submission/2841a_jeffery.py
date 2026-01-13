# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-12 14:55:40
# https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/
# IMPORTANT!! Submit Code Region End(Do not remove this line)


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        s = ans = 0
        t = list()
        for i, x in enumerate(nums):
            s += x
            t.append(x)
            # 这个题的窗口长度为k
            left = i - k + 1
            if left < 0:
                continue
            if len(set(t)) >= m:
                ans = max(s, ans)
            t.remove(t[0])
            s -= nums[left]
        return ans

# IMPORTANT!! Submit Code Region End(Do not remove this line)
