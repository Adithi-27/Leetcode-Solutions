# -*- coding: utf-8 -*-
"""441. Arranging Coins.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nOUn44tXxoD55j-RB3WonMde9MgWdNmP
"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0

        while l <= r:
            mid = (l + r) // 2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res