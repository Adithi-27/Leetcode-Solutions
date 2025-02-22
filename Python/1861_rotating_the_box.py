# -*- coding: utf-8 -*-
"""1861. Rotating the Box.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19_NyjNabR4t8oTzmBr9aE4hpQ1t6T057
"""

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])

        for r in range(rows):
            i = cols - 1
            for c in reversed(range(cols)):
                if box[r][c] == "#":
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                elif box[r][c] == "*":
                    i = c - 1

        rotated_box = []
        for c in range(cols):
            col = []
            for r in reversed(range(rows)):
                col.append(box[r][c])
            rotated_box.append(col)

        return rotated_box