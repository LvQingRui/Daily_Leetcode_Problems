# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
# Time: 2026-01-10 16:56:01
# https://leetcode.cn/problems/k-radius-subarray-averages/
# IMPORTANT!! Submit Code Region End(Do not remove this line)


# IMPORTANT!! Submit Code Region Begin(Do not remove this line)
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        avgs = [-1] * len(nums)
        s = 0
        for i, x in enumerate(nums):
            s += x
            left = i - 2 * k

            if left < 0:
                continue
            avgs[i - k] = s // (2 * k + 1)

            s -= nums[i - 2 * k]

        return avgs

    # IMPORTANT!! Submit Code Region End(Do not remove this line)


if __name__ == '__main__':
    s = Solution()
    print(s.getAverages([100000], 3))
