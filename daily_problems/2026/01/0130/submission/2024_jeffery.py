# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-30 20:48:34
# https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/
# IMPORTANT!! Submit Code Region End(Do not remove this line)
from collections import defaultdict


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = ans = 0
        cnt = defaultdict(int)
        for i, x in enumerate(answerKey):
            cnt[x] += 1
            while cnt['T'] > k and cnt['F'] > k:
                cnt[answerKey[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans
# IMPORTANT!! Submit Code Region End(Do not remove this line)
