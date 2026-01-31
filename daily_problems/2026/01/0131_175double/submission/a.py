"""
@File  :a.py
@Author:JefferyRuii
@Date  :2026/1/31 23:33
"""


class Solution:
    def reverseByType(self, s: str) -> str:
        chars = list(s)

        # 字母
        letters = [c for c in chars if c.isalpha()]
        letters.reverse()

        index = 0
        for i in range(len(chars)):
            if chars[i].isalpha():
                chars[i] = letters[index]
                index += 1

        # 字符
        zifu = [c for c in chars if not c.isalpha()]
        zifu.reverse()

        index = 0
        for i in range(len(chars)):
            if not chars[i].isalpha():
                chars[i] = zifu[index]
                index += 1

        return "".join(chars)
