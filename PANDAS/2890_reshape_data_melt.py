# -*- coding: utf-8 -*-
"""2890. Reshape Data: Melt.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iP24vtSYrykI5jEonykUHLSfRx77J41m
"""

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars='product', var_name='quarter', value_name='sales')