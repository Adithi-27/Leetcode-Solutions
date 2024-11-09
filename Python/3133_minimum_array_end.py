# -*- coding: utf-8 -*-
"""3133. Minimum Array End.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/167wSGl_Hc8ekF7wBry4RBBSe5M0tRtdb
"""

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        incr = n - 1
        ans = 0

        for i in range(64):
            if (x & (1 << i)) > 0:
                ans |= (1 << i)
            else:
                ans |= (((incr & 1) << i))
                incr >>= 1

        return ans