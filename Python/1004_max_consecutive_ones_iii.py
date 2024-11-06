# -*- coding: utf-8 -*-
"""1004. Max Consecutive Ones III.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11pDPqcnacs5XN5LXupPLvzHS1YBX5iJd
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_length = 0
        zeros_count = 0

        # Expand the window with the right pointer
        for right in range(len(nums)):
            # If we encounter a zero, increase the zero count
            if nums[right] == 0:
                zeros_count += 1

            # If zero count exceeds k, shrink the window from the left
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            # Update the maximum length of the window
            max_length = max(max_length, right - left + 1)

        return max_length