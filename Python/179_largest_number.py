# -*- coding: utf-8 -*-
"""179. Largest Number.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1faCIIy4DcvKIPFhe-6fKEts_pPyqy_PZ
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key = cmp_to_key(compare))
        return str(int("".join(nums)))