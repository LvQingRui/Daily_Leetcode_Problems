# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-11 00:13:02
# https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
# IMPORTANT!! Submit Code Region End(Do not remove this line)
import math


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt = 0
        ans = math.inf
        for i, c in enumerate(blocks):
            if c == 'W':
                cnt += 1
            left = i - k + 1

            if left < 0:
                continue

            ans = min(cnt, ans)

            if blocks[left] == "W":
                cnt -= 1
        return ans


# IMPORTANT!! Submit Code Region End(Do not remove this line)

if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumRecolors("WBBWWBBWBW", 7))
