# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-28 12:42:21
# https://leetcode.cn/problems/maximum-erasure-value/
# IMPORTANT!! Submit Code Region End(Do not remove this line)


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        sub = set()
        ans = left = s = 0
        for x in nums:
            while x in sub:
                sub.remove(nums[left])
                s -= nums[left]
                left += 1
            sub.add(x)
            s += x
            ans = max(s, ans)
        return ans


# IMPORTANT!! Submit Code Region End(Do not remove this line)
if __name__ == '__main__':
    s = Solution()
    print(s.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))  # 17
