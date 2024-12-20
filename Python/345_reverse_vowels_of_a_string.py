# -*- coding: utf-8 -*-
"""345. Reverse Vowels of a String.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TufaTxNCjBtSNhlVO8lSBYK89z-HZL4J
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define a set of vowels (both uppercase and lowercase)
        vowels = set("aeiouAEIOU")
        # Convert the string to a list to allow modifications
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            # Move the left pointer to the next vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move the right pointer to the previous vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            # Swap the vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        # Join the list back into a string
        return "".join(s_list)