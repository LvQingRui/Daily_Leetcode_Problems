# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-02-01 20:13:25
# https://leetcode.cn/problems/count-monobit-integers/
# IMPORTANT!! Submit Code Region End(Do not remove this line)


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def countMonobit(self, n: int) -> int:
        count = 1
        x = 1

        while x <= n:
            count += 1
            x = (x << 1) | 1

        return count


# IMPORTANT!! Submit Code Region End(Do not remove this line)
