"""
@File  :lc1343_jeffery.py
@Author:JefferyRuii
@Date  :2026/1/9 13:16
"""


def main(arr: list[int], k: int, threshold: int) -> int:
    count = s = 0
    for i, x in enumerate(arr):
        s += x
        left = i - k + 1

        if left < 0:
            continue
        if (s / k) >= threshold:
            count += 1

        s -= arr[left]
    return count


if __name__ == '__main__':
    print(main([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
    print(main([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
