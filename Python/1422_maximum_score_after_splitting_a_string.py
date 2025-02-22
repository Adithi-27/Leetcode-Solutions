# -*- coding: utf-8 -*-
"""1422. Maximum Score After Splitting a String.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nOUn44tXxoD55j-RB3WonMde9MgWdNmP
"""

class Solution:
    def maxScore(self, s: str) -> int:
        l, r = 0, s.count("1")
        ans = 0
        for x in s[:-1]:
            l += int(x) ^ 1
            r -= int(x)
            ans = max(ans, l + r)
        return ans