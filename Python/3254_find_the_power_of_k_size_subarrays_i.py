# -*- coding: utf-8 -*-
"""3254. Find the Power of K-Size Subarrays I.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1URvySlkRixdVynBRUFyD-G3T-HN_h2g3
"""

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)

        streak = 0
        ans = []
        for i in range(N):
            if i >= 1 and nums[i] == nums[i - 1] + 1:
                streak += 1
            else:
                streak = 1

            if i >= k - 1:
                if streak >= k:
                    ans.append(nums[i])
                else:
                    ans.append(-1)
        return ans