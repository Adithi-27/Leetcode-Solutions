# -*- coding: utf-8 -*-
"""2601. Prime Subtraction Operation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DJlNJzkS8JSf7UQ-ur0ndSoHlkwT4INx
"""

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    return False
            return True

        prev = 0
        for n in nums:
            upper_bound = n - prev

            largest_p = 0
            for i in reversed(range(2, upper_bound)):
                if is_prime(i):
                    largest_p = i
                    break

            if n - largest_p <= prev:
                return False
            prev = n - largest_p

        return True