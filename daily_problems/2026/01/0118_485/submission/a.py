"""
@File  :a.py
@Author:JefferyRuii
@Date  :2026/1/18 10:31
"""


# https://leetcode.cn/problems/vowel-consonant-score/


def vowelConsonantScore(self, s: str) -> int:
    vowels = 'aeiou'
    v = 0
    c = 0
    for ch in s:
        if not ch.isalpha():
            continue
        if ch in vowels:
            v += 1
        else:
            c += 1

    return v // c if c else 0
