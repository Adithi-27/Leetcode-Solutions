# -*- coding: utf-8 -*-
"""2878. Get the Size of a DataFrame.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iP24vtSYrykI5jEonykUHLSfRx77J41m
"""

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    row, col = players.shape
    return[row, col]