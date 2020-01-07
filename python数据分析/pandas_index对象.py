"""
本文讲解了如下内容
1.index对象的方法
2.含有重复标签的index
"""

import pandas as pd

ser = pd.Series([5, 0, 3, 8, 4], index=['red', 'blue', 'yellow', 'white', 'green'])
print(ser)
"""
red       5
blue      0
yellow    3
white     8
green     4
dtype: int64
"""
print(ser.index)
"""
Index(['red', 'blue', 'yellow', 'white', 'green'], dtype='object')
"""

# index对象内置方法
# idmin()索引值最小
# idmax()索引值最大
# print(ser.idxmin())  # blue
# print(ser.idxmax())  # white


# 含有重复标签的index
serd = pd.Series(range(6), index=['white', 'white', 'blue', 'green', 'green', 'yellow'])
print(serd)
"""
white     0
white     1
blue      2
green     3
green     4
yellow    5
dtype: int64
"""

# 从数据结构中选取元素时，如果一个标签对应多个元素，我们得到的将是一个Series对象而不是单个元素
print(serd['white'])
"""
white    0
white    1
dtype: int64
"""
# 以上逻辑适用于索引中存在重复项的DataFrame，其返回结果为DataFrame对象

# is_unique   调用该属性，就可以知道数据结构（Series和DataFrame）中是否存在重复的索引项
print(serd.index.is_unique)  # False
