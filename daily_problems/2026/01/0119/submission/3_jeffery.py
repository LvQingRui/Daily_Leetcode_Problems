# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-19 00:11:37
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# IMPORTANT!! Submit Code Region End(Do not remove this line)
from collections import defaultdict


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        cnt = defaultdict(int)

        for right, x in enumerate(s):
            cnt[x] += 1

            while cnt[x] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
# IMPORTANT!! Submit Code Region End(Do not remove this line)
