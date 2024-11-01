# -*- coding: utf-8 -*-
"""151. Reverse Words in a String.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G53d8ldaKirzFE2yKgVxPTKog5sltaZ0
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by spaces which also removes extra spaces automatically
        words = s.split()

        # Reverse the list of words
        words.reverse()

        # Join the reversed list of words with a single space separator
        return ' '.join(words)