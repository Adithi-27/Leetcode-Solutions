# -*- coding: utf-8 -*-
"""153. Find Minimum in Rotated Sorted Array.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_FyJWqF9g_z2lnoeCSP-fPR_aooACFB1
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res