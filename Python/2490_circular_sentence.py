# -*- coding: utf-8 -*-
"""2490. Circular Sentence.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Cr7W4kpBRfyE7AQYY_7Low_8ypzz8HOs
"""

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        N = len(words)

        for left in range(N):
            right = (left + 1) % N
            if words[left][-1] != words[right][0]:
                return False

        return True