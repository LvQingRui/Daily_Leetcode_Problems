# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-23 07:05:20
# https://leetcode.cn/problems/get-equal-substrings-within-budget/
# IMPORTANT!! Submit Code Region End(Do not remove this line)


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost_s = 0
        left = 0
        ans = 0
        for right, x in enumerate(s):
            cost_s += abs(ord(s[right]) - ord(t[right]))
            while cost_s > maxCost:
                cost_s -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans

# IMPORTANT!! Submit Code Region End(Do not remove this line)
