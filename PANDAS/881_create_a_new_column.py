# -*- coding: utf-8 -*-
"""881. Create a New Column.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iP24vtSYrykI5jEonykUHLSfRx77J41m
"""

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']*2
    return employees