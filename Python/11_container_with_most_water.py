# -*- coding: utf-8 -*-
"""11. Container With Most Water.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1faCIIy4DcvKIPFhe-6fKEts_pPyqy_PZ
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res