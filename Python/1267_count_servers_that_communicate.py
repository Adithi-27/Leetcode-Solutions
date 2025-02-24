# -*- coding: utf-8 -*-
"""1267. Count Servers that Communicate.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hZY38eysGcNm88W8iNVqAhduj33Gr8yT
"""

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
        return sum(
            grid[i][j] and (row[i] > 1 or col[j] > 1)
            for i in range(m)
            for j in range(n)
        )