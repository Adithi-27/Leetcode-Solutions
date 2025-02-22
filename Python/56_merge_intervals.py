# -*- coding: utf-8 -*-
"""56. Merge Intervals.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1faCIIy4DcvKIPFhe-6fKEts_pPyqy_PZ
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastend = output[-1][1]

            if start <= lastend:
                output[-1][1] = max(lastend, end)
            else:
                output.append([start, end])
        return output