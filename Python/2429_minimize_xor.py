# -*- coding: utf-8 -*-
"""2429. Minimize XOR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1faCIIy4DcvKIPFhe-6fKEts_pPyqy_PZ
"""

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt = num2.bit_count()
        x = 0
        for i in range(30, -1, -1):
            if num1 >> i & 1 and cnt:
                x |= 1 << i
                cnt -= 1
        for i in range(30):
            if num1 >> i & 1 ^ 1 and cnt:
                x |= 1 << i
                cnt -= 1
        return x