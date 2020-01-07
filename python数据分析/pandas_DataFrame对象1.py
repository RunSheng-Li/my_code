"""
本文件讲解了如下内容：
1.定义DataFrame对象
2.选取元素
3.赋值
4.元素的所属关系
5.删除一列
6.筛选
"""
import numpy as np
import pandas as pd

# 定义DataFrame对象
# 新建DataFrame对象的最常用方法是传递一个dict对象给DataFrame()构造函数。dict对象以每一列的名称作为键，每个键都有一个数组作为值

data = {
    'color': ['blue', 'green', 'yellow', 'red', 'white'],
    'object': ['ball', 'pen', 'pencil', 'paper', 'mug'],
    'price': [1.2, 1.0, 0.6, 0.9, 1.7]
}

frame = pd.DataFrame(data)
print(frame)
"""
    color  object  price
0    blue    ball    1.2
1   green     pen    1.0
2  yellow  pencil    0.6
3     red   paper    0.9
4   white     mug    1.7
"""

# 如果用来创建DataFrame对象的dict对象包含一些用不到的数据，可以选择自己感兴趣的
# 在DataFrame构造函数中，用columns选项指定需要的列即可
# 新建的DataFrame各列顺序与你指定的列顺序一致，而与它们在字典中的顺序无关

frame2 = pd.DataFrame(data, columns=['object', 'price'])
# print(frame2)
"""
   object  price
0    ball    1.2
1     pen    1.0
2  pencil    0.6
3   paper    0.9
4     mug    1.7
"""

# DataFrame对象跟Series一样，如果Index数组没有明确指定标签，pandas也会自动为其添加一列从0开始的数值作为索引
# 如果想用标签作为DataFrame的索引，则要把标签放到数组中，赋给index选项

frame2 = pd.DataFrame(data, index=['one', 'two', 'three', 'four', 'five'])
# print(frame2)
"""
        color  object  price
one      blue    ball    1.2
two     green     pen    1.0
three  yellow  pencil    0.6
four      red   paper    0.9
five    white     mug    1.7
"""

# 还有一种定义DataFrame的新方法
# 我们不再使用dict对象，而是定义一个构造函数，指定三个参数：数据矩阵、index选项、colums选项

frame3 = pd.DataFrame(np.arange(16).reshape((4, 4)),
                      index=['red', 'blue', 'yellow', 'white'],
                      columns=['ball', 'pen', 'pencil', 'paper'])
# print(frame3)
"""
        ball  pen  pencil  paper
red        0    1       2      3
blue       4    5       6      7
yellow     8    9      10     11
white     12   13      14     15
"""

# 选取元素

# 如果想知道DataFrame对象所有列的名称，在它上面调用columns属性即可
# print(frame.columns)  # Index(['color', 'object', 'price'], dtype='object')

# 要获取索引列表，调用index属性即可
# print(frame.index)  # RangeIndex(start=0, stop=5, step=1)

# 如果要获取存储在数据结构中的元素，可以使用values属性获取所有元素
# print(frame.values)
"""
[['blue' 'ball' 1.2]
 ['green' 'pen' 1.0]
 ['yellow' 'pencil' 0.6]
 ['red' 'paper' 0.9]
 ['white' 'mug' 1.7]]
"""

# 如果想选择一列内容，把这一列的名称作为索引即可
# print(frame['price'])
# print(type(frame['price'])) # <class 'pandas.core.series.Series'>

# 另外一种方法
# print(frame.price)

# 至于DataFrame中的行，用ix属性和行的索引值就能获取到
# print(frame.ix[2])
"""
color     yellow
object    pencil
price        0.6
Name: 2, dtype: object
"""

# 用一个数组制定多个索引值就能选取多行
# print(frame.ix[[2, 4]])


# 若要从DataFrame抽取一部分，可以用索引值选择你想要的行。通过指定索引范围来选取，其中这一行的索引作为起始索引值，下一行的索引作为结束索引
# print(frame[0:1])

# 如需多行，则需要扩展选择范围
# print(frame[1:3])

# 如果要获取存储在DataFrame中的一个元素，需要依次指定元素所在的列名称，行的索引值或标签
# print(frame['object'][3])  # paper

# 赋值
# index属性指定DataFrame结构中的索引数组，用columns属性指定包含列名称的行
frame.index.name = 'id'
frame.columns.name = 'item'
print(frame)
"""
item   color  object  price
id                         
0       blue    ball    1.2
1      green     pen    1.0
2     yellow  pencil    0.6
3        red   paper    0.9
4      white     mug    1.7
"""

# 添加列 指定DataFrame实例新列的名称，为其赋值即可
frame['new'] = 12
# print(frame)
"""
item   color  object  price  new
id                              
0       blue    ball    1.2   12
1      green     pen    1.0   12
2     yellow  pencil    0.6   12
3        red   paper    0.9   12
4      white     mug    1.7   12
"""

# 然而，如果想更新一列的内容，需要把一个数组赋值给这一列
frame['new'] = [3.0, 1.3, 2.2, 0.8, 1.1]
# print(frame)
"""
item   color  object  price  new
id                              
0       blue    ball    1.2  3.0
1      green     pen    1.0  1.3
2     yellow  pencil    0.6  2.2
3        red   paper    0.9  0.8
4      white     mug    1.7  1.1
"""

# 为DataFrame的各列赋一个Series对象也可以创建DataFrame
ser = pd.Series(np.arange(5))
frame['new'] = ser
# print(frame)
"""
item   color  object  price  new
id                              
0       blue    ball    1.2    0
1      green     pen    1.0    1
2     yellow  pencil    0.6    2
3        red   paper    0.9    3
4      white     mug    1.7    4
"""

# 修改单个元素的方法：选择元素，为其赋新值即可
frame['price'][2] = 3.3
# print(frame)
"""
item   color  object  price  new
id                              
0       blue    ball    1.2    0
1      green     pen    1.0    1
2     yellow  pencil    3.3    2
3        red   paper    0.9    3
4      white     mug    1.7    4

"""

# 元素的所属关系

# print(frame.isin([1.0, 'pen']))
"""
item  color  object  price    new
id                               
0     False   False  False  False
1     False    True   True   True
2     False   False  False  False
3     False   False  False  False
4     False   False  False  False
"""

# print(frame[frame.isin([1.0, 'pen'])])
"""
item color object  price  new
id                           
0      NaN    NaN    NaN  NaN
1      NaN    pen    1.0  1.0
2      NaN    NaN    NaN  NaN
3      NaN    NaN    NaN  NaN
4      NaN    NaN    NaN  NaN
"""

# 删除一列

del frame['new']
print(frame)
"""
item   color  object  price
id                         
0       blue    ball    1.2
1      green     pen    1.0
2     yellow  pencil    3.3
3        red   paper    0.9
4      white     mug    1.7
"""

# 筛选
# 这个不知道为什么会报错
# print(frame[frame < 12])
