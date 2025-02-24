# -*- coding: utf-8 -*-
"""90. Subsets II.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fpVFyNM24h-nF9dKZx0842SxfCalg1_e
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # all subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res