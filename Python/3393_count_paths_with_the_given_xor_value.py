# -*- coding: utf-8 -*-
"""3393. Count Paths With the Given XOR Value.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_FyJWqF9g_z2lnoeCSP-fPR_aooACFB1
"""

class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        M = 10**9 + 7
        x = len(grid)
        y = len(grid[0])
        m_Xor = 15

        # Initialize 3D DP array with zeros
        dp = [[[0] * (m_Xor + 1) for _ in range(y)] for _ in range(x)]

        # Initialize starting position
        dp[0][0][grid[0][0]] = 1

        # Fill the DP array
        for a in range(x):
            for b in range(y):
                for xorVal in range(m_Xor + 1):
                    if dp[a][b][xorVal] > 0:
                        # Move right
                        if b + 1 < y:
                            n_Xor = xorVal ^ grid[a][b + 1]
                            dp[a][b + 1][n_Xor] = (dp[a][b + 1][n_Xor] + dp[a][b][xorVal]) % M

                        # Move down
                        if a + 1 < x:
                            n_Xor = xorVal ^ grid[a + 1][b]
                            dp[a + 1][b][n_Xor] = (dp[a + 1][b][n_Xor] + dp[a][b][xorVal]) % M

        return dp[x - 1][y - 1][k]