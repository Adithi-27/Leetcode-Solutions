# -*- coding: utf-8 -*-
"""3. Longest Substring Without Repeating Characters.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1URvySlkRixdVynBRUFyD-G3T-HN_h2g3
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1

            char_index_map[char] = end

            max_length = max(max_length, end - start + 1)

        return max_length