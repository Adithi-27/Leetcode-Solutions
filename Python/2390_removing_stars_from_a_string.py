# -*- coding: utf-8 -*-
"""2390. Removing Stars From a String.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YCO466HUMIjHuuvqo8enqaqT7Ifz9mBo
"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)