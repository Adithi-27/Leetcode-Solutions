# -*- coding: utf-8 -*-
"""2070. Most Beautiful Item for Each Query.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zzNzNMOuXqVkGxnghTVgFuDUXgtDtMpf
"""

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([(q, i) for i, q in enumerate(queries)])

        res = [0] * len(queries)
        max_bae = 0
        j = 0
        for q, i in queries:
            while j < len(items) and items[j][0] <= q:
                max_bae = max(max_bae, items[j][1])
                j += 1

            res[i] = max_bae

        return res