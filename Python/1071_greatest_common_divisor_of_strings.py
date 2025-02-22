# -*- coding: utf-8 -*-
"""1071. Greatest Common Divisor of Strings.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bocA_m9ivnk8zQWTlzEYbxbuhXBvx72H
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            # Check if lengths are divisible by l
            if len1 % l != 0 or len2 % l != 0:
                return False
            # Calculate the number of times the substring should repeat
            f1, f2 = len1 // l, len2 // l
            # Check if the substring can construct both strings
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        # Start from the minimum length and reduce
        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]

        return ""