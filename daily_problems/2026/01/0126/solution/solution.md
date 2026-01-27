这道题其实就应该注意 pairwise 这个函数的用法，他最常见、最标准的来源是Python 3.10+的：

```python
from itertools import pairwise
```

一句话总结就是：
pairwise(iterable) → 依次返回相邻的 (前一个, 后一个)

---


例子：

```python
from itertools import pairwise

nums = [1, 3, 6, 10]

print(list(pairwise(nums)))
```

输出：

```
[(1, 3), (3, 6), (6, 10)]
```
