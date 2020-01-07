import numpy as np
import pandas as pd

# 拼接

# numpy的concatenate()函数就是用于数组的拼接
array1 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# print(array1)

array2 = np.arange(9).reshape((3, 3)) + 6
# print(array2)
# print(np.concatenate([array1, array2], axis=1))
# print(np.concatenate([array1, array2], axis=0))

# pandas的concat()函数实现了按轴拼接的功能

ser1 = pd.Series(np.random.rand(4), index=[1, 2, 3, 4])
print(ser1)

ser2 = pd.Series(np.random.rand(4), index=[5, 6, 7, 8])
# print(ser2)

# print(pd.concat([ser1, ser2]))

# concat()函数默认按照axis=0这条轴拼接数据，返回Series对象。如果指定axis=1，返回结果将是DataFrame对象
# print(pd.concat([ser1, ser2], axis=1))

# DataFrame对象的拼接方法与之相同

frame1 = pd.DataFrame(np.random.rand(9).reshape(3, 3), index=[1, 2, 3], columns=['A', 'B', 'C'])
frame2 = pd.DataFrame(np.random.rand(9).reshape(3, 3), index=[4, 5, 6], columns=['A', 'B', 'C'])
# print(pd.concat([frame1, frame2]))
# print(pd.concat([frame1, frame2], axis=1))


# 组合
# 还有一种情况，我们无法通过合并或拼接方法组合数据。例如，两个数据集的索引完全或部分重合
ser1 = pd.Series(np.random.rand(5), index=[1, 2, 3, 4, 5])
# print(ser1)

ser2 = pd.Series(np.random.rand(4), index=[2, 4, 5, 6])
# print(ser2)

# print(ser1.combine_first(ser2))
# print(ser2.combine_first(ser1))

# 如果想进行部分合并，仅指定要合并的部分即可
# print(ser1[:3].combine_first(ser2[:3]))

# 轴向旋转


