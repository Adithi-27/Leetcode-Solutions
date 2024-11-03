# -*- coding: utf-8 -*-
"""796. Rotate String.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FM_kaGMZPd-mavYBtJ7n48_SnExZYqRy
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if lengths are equal
        if len(s) != len(goal):
            return False

        # Double the string and check if `goal` is a substring
        s = s + s
        return goal in s