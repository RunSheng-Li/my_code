"""
本文件讲解了如下内容
1.用嵌套字典生成DataFrame对象
2.DataFrame转置
"""

import pandas as pd


# 嵌套字典是python广泛使用的数据结构，如下
# 直接将这种数据结构作为参数传递给DataFrame()构造函数，pandas就会将外部的键解释成列名称，将内部的键解释为索引标签
# 解释嵌套结构时，可能并非所有位置都有相应的元素存在，pandas会用NaN填补缺失的元素
nestdict = {
    'red': {2012: 22, 2013: 33},
    'white': {2011: 13, 2012: 22, 2013: 16},
    'blue': {2011: 17, 2012: 27, 2013: 18}
}

frame2 = pd.DataFrame(nestdict)
print(frame2)
"""
       red  white  blue
2012  22.0     22    27
2013  33.0     16    18
2011   NaN     13    17
"""

# DataFrame转置
print(frame2.T)
"""
       2012  2013  2011
red    22.0  33.0   NaN
white  22.0  16.0  13.0
blue   27.0  18.0  17.0
"""



