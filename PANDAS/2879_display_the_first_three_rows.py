# -*- coding: utf-8 -*-
"""2879. Display the First Three Rows.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iP24vtSYrykI5jEonykUHLSfRx77J41m
"""

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)