# -*- coding: utf-8 -*-
"""2886. Change Data Type.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iP24vtSYrykI5jEonykUHLSfRx77J41m
"""

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students