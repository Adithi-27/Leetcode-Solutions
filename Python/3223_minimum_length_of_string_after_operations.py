# -*- coding: utf-8 -*-
"""3223. Minimum Length of String After Operations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1faCIIy4DcvKIPFhe-6fKEts_pPyqy_PZ
"""

class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)
        return sum(1 if x & 1 else 2 for x in cnt.values())