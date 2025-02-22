# -*- coding: utf-8 -*-
"""3042. Count Prefix and Suffix Pairs I.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nOUn44tXxoD55j-RB3WonMde9MgWdNmP
"""

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i, s in enumerate(words):
            for t in words[i + 1 :]:
                ans += t.endswith(s) and t.startswith(s)
        return ans