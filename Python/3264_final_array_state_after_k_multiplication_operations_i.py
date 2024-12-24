# -*- coding: utf-8 -*-
"""3264. Final Array State After K Multiplication Operations I.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_FyJWqF9g_z2lnoeCSP-fPR_aooACFB1
"""

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier
        return nums