"""
@File  :b.py
@Author:JefferyRuii
@Date  :2026/2/1 20:14
"""


class Solution:
    def finalElement(self, nums: list[int]) -> int:
        return max(nums[0], nums[-1])
