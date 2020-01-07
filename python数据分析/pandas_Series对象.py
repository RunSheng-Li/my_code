"""
本文件讲解了如下内容
1.声明Series对象
2.选择内部元素
3.为元素赋值
4.用Numpy数组或其他Series对象定义新Series对象
5.筛选元素
6.Series对象运算和数学函数
7.Series对象的组成元素
8.NaN
9.Series用作字典
10.Series对象之间的运算

"""
import numpy as np
import pandas as pd

# 声明Series对象
# 调用Series()构造函数，把要存放在Series对象中的数据以数组形式传入，就能创建一个Series对象

s = pd.Series([12, -4, 7, 9])
# print(s)
"""
输出如下：

0    12
1    -4
2     7
3     9
dtype: int64

左侧index是一列标签，右侧是标签对应的元素
声明Series时，如果不指定标签，pandas默认使用从0开始依次递增的数值作为标签
"""

# 最好使用有意义的标签，用以区分和识别每个元素
# 因此，调用构造函数时，就需要指定index选项，把存放有标签的数组赋给它，其中标签为字符串类型

s = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
# print(s)
"""
输出如下：
a    12
b    -4
c     7
d     9
dtype: int64
"""

# 如果想分别查看组成Series对象的两个数组，可以调用它的两个属性：index（索引）和 values（元素）
# print(s.values)  # 输出：[12 -4  7  9]
# print(s.index)  # 输出：Index(['a', 'b', 'c', 'd'], dtype='object')


# 选择内部元素
# 若想获取Series对象内部的元素，把它作为普通的Numpy数组，指定键即可
# print(s[2])  # 输出： 7
# print(s['b'])  # 输出：-4

# 跟从NUmpy数组选择多个元素的方法相同，可像下面这样选取多项
# print(s[0:2])
"""
输出：
a    12
b    -4
dtype: int64
"""

# 或者这种情况设置可以使用元素对应的标签，只不过要把标签放到数组中
# print(s[["b", "d"]])
"""
输出：
b   -4
d    9
dtype: int64
"""

# 为元素赋值
# 可以用索引或者标签选取元素后进行赋值
s[1] = 0
# print(s)
"""
a    12
b     0
c     7
d     9
dtype: int64
"""
s['b'] = 1
# print(s)
"""
a    12
b     1
c     7
d     9
dtype: int64
"""

# 用Numpy数组或其他Series对象定义新Series对象

arr = np.array([1, 2, 3, 4])
s3 = pd.Series(arr)
# print(s3)
"""
0    1
1    2
2    3
3    4
dtype: int32
"""

s4 = pd.Series(s)
# print(s4)
"""
a    12
b     1
c     7
d     9
dtype: int64
"""

# 然后,这样做不要忘了，新Series对象中的元素不是原Numpy数组或Series对象元素的副本，而是对他们的引用
# 也就是说，如改变原有对象的值，新Series对象中这些元素也会发生变化
# 如下：改动arr数组第三个元素的值，同时也会修改Series对象s3中相应的元素
arr[2] = -2
# print(s3)
"""
0    1
1    2
2   -2
3    4
dtype: int32
"""

# 筛选元素
# 要获取Series对象中所有大于8的元素
# print(s[s > 8])
"""
输出：
a    12
d     9
dtype: int64
"""

# Series对象运算和数学函数
# 适用于Numpy数组的运算符或其他数学函数，也适用于Series对象
# print(s / 2)
"""
a    6.0
b    0.5
c    3.5
d    4.5
dtype: float64
"""

# 至于Numpy库的数学函数，必须制定它们的出处np，并把Series实例作为参数传入
# print(np.log(s))
"""
a    2.484907
b    0.000000
c    1.945910
d    2.197225
dtype: float64
"""

# Series对象的组成元素
serd = pd.Series([1, 0, 2, 1, 2, 3], index=['white', 'white', 'blue', 'green', 'green', 'yellow'])
# print(serd)
"""
white     1
white     0
blue      2
green     1
green     2
yellow    3
dtype: int64
"""

# 要弄清楚Series对象包含多少个不同的元素，可使用unique()函数。其返回结果为一个数组，包含Series去重后的元素，但顺序看上去很随意
# print(serd.unique())  # [1 0 2 3]

# value_counts()函数，它不仅返回各个不同的元素还计算每个元素在Series中出现的次数
# print(serd.value_counts())
"""
2    2
1    2
3    1
0    1
dtype: int64
"""

# isin()函数用来判断所属关系，也就是判断给定的一列元素是否包含在数据结构之中
# isin()函数返回布尔值，可用于筛选Series或DataFrame列中的数据
# print(serd.isin([0, 3]))
"""
white     False
white      True
blue      False
green     False
green     False
yellow     True
dtype: bool
"""
# print(serd[serd.isin([0, 3])])
"""
white     0
yellow    3
dtype: int64
"""

# NaN
# 如果是NaN，isnull()函数返回值为True
# 如果不是NaN，notnull()函数返回值为True
s2 = pd.Series([5, -3, np.NaN, 14])
# print(s2)
"""
0     5.0
1    -3.0
2     NaN
3    14.0
dtype: float64
"""
# print(s2.isnull())
"""
0    False
1    False
2     True
3    False
dtype: bool
"""
# print(s2.notnull())
"""
0     True
1     True
2    False
3     True
dtype: bool
"""

# print(s2[s2.notnull()])
"""
0     5.0
1    -3.0
3    14.0
dtype: float64
"""

# print(s2[s2.isnull()])
"""
2   NaN
dtype: float64
"""

# Series用作字典

mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}
myseries = pd.Series(mydict)
# print(myseries)
"""
red       2000
blue      1000
yellow     500
orange    1000
dtype: int64
"""
# 如遇缺失值处，pandas就会为其添加NaN
colors = ['red', 'yellow', 'orange', 'blue', 'green']
myseries = pd.Series(mydict, index=colors)
print(myseries)
"""
red       2000.0
yellow     500.0
orange    1000.0
blue      1000.0
green        NaN
dtype: float64
"""

# Series对象之间的运算
# 只对标签相同的元素求和。其他只属于任何一个Series对象的标签也被添加到新对象中，只不过它们的值均为NaN
mydict2 = {'red': 400, 'yellow': 1000, 'black': 700}
myseries2 = pd.Series(mydict2)
print(myseries + myseries2)
"""
black        NaN
blue         NaN
green        NaN
orange       NaN
red       2400.0
yellow    1500.0
dtype: float64
"""
