# -*- coding: utf-8 -*-
"""3392. Count Subarrays of Length Three With a Condition.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_FyJWqF9g_z2lnoeCSP-fPR_aooACFB1
"""

class Solution:
    def countSubarrays(self, nums):
        a = 0
        b = 0
        r = 0

        while b < len(nums):
            if b - a + 1 >= 3:
                if (nums[a] + nums[b]) * 2 == nums[a + 1]:
                    r += 1
                a += 1
            b += 1

        return r