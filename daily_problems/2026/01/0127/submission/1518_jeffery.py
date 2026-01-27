# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-27 21:27:26
# https://leetcode.cn/problems/water-bottles/
# IMPORTANT!! Submit Code Region End(Do not remove this line)


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        while numBottles >= numExchange:
            ans += numExchange
            numBottles -= numExchange - 1
        return ans + numBottles


# IMPORTANT!! Submit Code Region End(Do not remove this line)


if __name__ == '__main__':
    s = Solution()
    print(s.numWaterBottles(15, 4))
