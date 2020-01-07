import pandas as pd

# 更换索引
ser = pd.Series([2, 5, 7, 4], index=['one', 'two', 'three', 'four'])
print(ser)
"""
one      2
two      5
three    7
four     4
dtype: int64
"""

# reindex
print(ser.reindex(['three', 'four', 'five', 'one']))
"""
three    7.0
four     4.0
five     NaN
one      2.0
dtype: float64
"""
