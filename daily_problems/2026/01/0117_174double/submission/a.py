"""
@File  :a.py
@Author:JefferyRuii
@Date  :2026/1/17 22:14
"""
import math


def bestTower(towers: list[list[int]], center: list[int], radius: int) -> list[int]:
    max_q = -math.inf
    ans = [-1, -1]
    cx, cy = center

    for x, y, q in towers:
        if abs(x - cx) + abs(y - cy) <= radius:
            if q > max_q:
                max_q = q
                ans = [x, y]
            elif q == max_q:
                if ans == [-1, -1] or [x, y] < ans:
                    ans = [x, y]

    return ans


if __name__ == '__main__':
    print(bestTower([[1, 3, 4], [2, 2, 4], [4, 4, 7]], [0, 0], 5))
