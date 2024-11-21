# -*- coding: utf-8 -*-
"""2257. Count Unguarded Cells in the Grid.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QcUJ9JgoQAqZZyko79Uz7yzByRrsyfAW
"""

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        for row, col in walls:
            grid[row][col] = 1
        for row, col in guards:
            grid[row][col] = 2

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for row, col in guards:
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < m and 0 <= c < n and grid[r][c] != 1 and grid[r][c] != 2:
                    if grid[r][c] == 0:
                        grid[r][c] = 3
                    r += dr
                    c += dc

        unguarded_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    unguarded_count += 1

        return unguarded_count