# -*- coding: utf-8 -*-
"""1957. Delete Characters to Make Fancy String.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G53d8ldaKirzFE2yKgVxPTKog5sltaZ0
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for c in s:
            stack.append(c)

            if len(stack) >= 3 and (stack[-1] == stack[-2] == stack[-3]):
                stack.pop()
        return "".join(stack)