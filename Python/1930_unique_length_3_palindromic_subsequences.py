# -*- coding: utf-8 -*-
"""1930. Unique Length-3 Palindromic Subsequences.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nOUn44tXxoD55j-RB3WonMde9MgWdNmP
"""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for c in ascii_lowercase:
            l, r = s.find(c), s.rfind(c)
            if r - l > 1:
                ans += len(set(s[l + 1 : r]))
        return ans