# -*- coding: utf-8 -*-
"""3105. Longest Strictly Increasing or Strictly Decreasing Subarray.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nHooiJVSGNXBCJeoSWF9eIncC0IoVGRw
"""

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = t = 1
        for i, x in enumerate(nums[1:]):
            if nums[i] < x:
                t += 1
                ans = max(ans, t)
            else:
                t = 1
        t = 1
        for i, x in enumerate(nums[1:]):
            if nums[i] > x:
                t += 1
                ans = max(ans, t)
            else:
                t = 1
        return ans