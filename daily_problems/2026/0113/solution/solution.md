下面的这种写法直接tle了，关键点在于：`if len(set(a)) == k:`这段代码，`set(a)` 每次都会重新遍历整个 `a`,而 `a`的长度最多为
`k`, 所以下面的这段代码的时间复杂度是
O(n * k), 而ac了的代码dict的size()是O(1)的，所以时间复杂度是O(n)的，所以不会tle。。。 和0112写的题 思路类似。

```python
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_s = s = 0
        n = len(nums)
        a = []
        for i, x in enumerate(nums):
            s += x
            a.append(x)

            left = i - k + 1
            if left < 0:
                continue
            if len(set(a)) == k:
                max_s = max(s, max_s)
                s -= nums[left]
                a.remove(a[0])
            else:
                s -= nums[left]
                a.remove(a[0])

        return max_s
```