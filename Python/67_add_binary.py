# -*- coding: utf-8 -*-
"""67. Add Binary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hZY38eysGcNm88W8iNVqAhduj33Gr8yT
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digita = ord(a[i]) - ord("0") if i < len(a) else 0
            digitb = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digita + digitb + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2

        if carry:
            res = "1" + res
        return res