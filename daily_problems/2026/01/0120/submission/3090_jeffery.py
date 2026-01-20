# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-20 11:50:11
# https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/
# IMPORTANT!! Submit Code Region End(Do not remove this line)
from collections import defaultdict


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        cnt = defaultdict(int)
        left = 0
        for right, x in enumerate(s):
            cnt[x] += 1
            while cnt[x] > 2:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumLengthSubstring("bcbbbcba"))
