# -*- coding: utf-8 -*-
"""443. String Compression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G53d8ldaKirzFE2yKgVxPTKog5sltaZ0
"""

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Points to where we write in the chars array
        read = 0   # Points to where we read in the chars array

        while read < len(chars):
            # Start of a sequence of the same character
            char = chars[read]
            count = 0

            # Count the number of occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # Return the new length of the compressed list
        return write