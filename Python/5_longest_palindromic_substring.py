# -*- coding: utf-8 -*-
"""5. Longest Palindromic Substring.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vJfJbfBv9tG-yJwm60w_ZURVjkJlDkeV
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            # Expand around the center as long as it's a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring
            return s[left + 1:right]

        longest_palindrome = ""

        for i in range(len(s)):
            # Check for odd-length palindromes
            odd_palindrome = expand_around_center(i, i)
            # Check for even-length palindromes
            even_palindrome = expand_around_center(i, i + 1)

            # Update the longest palindrome found
            longest_palindrome = max(longest_palindrome, odd_palindrome, even_palindrome, key=len)

        return longest_palindrome