# -*- coding: utf-8 -*-
"""2275. Largest Combination With Bitwise AND Greater Than Zero.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ETlWXiqQWsEYI89yxCzH-avauT8-EHfo
"""

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0] * 32

        for n in candidates:
            i = 0
            while n > 0:
                count[i] += 1 & n
                i += 1
                n = n >> 1
        return max(count)