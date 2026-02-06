class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_s = left = 0
        for right, x in enumerate(nums):
            while nums[left] * k < x:
                left += 1
            max_s = max(max_s, right - left + 1)
        return len(nums) - max_s
