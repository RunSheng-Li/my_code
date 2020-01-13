import numpy as np

# ndarray:numpy库的心脏
# ------------------------------------------------------------------------------

# numpy数组的一个特点是大小固定，也就是说，创建数组时一旦指定好大小，就不会再发生改变。这与python的列表有所不同，列表的大小是可以改变的
# 定义ndarray最简单的方式是array()函数，以python列表作为参数，列表的元素即是ndarray的元素
a = np.array([1, 2, 3])
# print(a)

# 检测对象是否是ndarray
# print(type(a))

# 调用变量的dtype属性，即可获知新建的ndarray属于哪种数据类型
# print(a.dtype)

# 轴数
# print(a.ndim)

# 数组长度
# print(a.size)

# 数组的型
# print(a.shape)

# 定义2*2的二维数组
b = np.array([[1.3, 2.4], [0.3, 4.1]])
# print(b.dtype)
# print(b.ndim)
# print(b.shape)
# 定义了数组每个元素的长度为几个字节
# print(b.itemsize)
# print(b.data)

# ------------------------------------------------------------------------------


# 创建数组
# ------------------------------------------------------------------------------

# 单层或嵌套列表
c = np.array([[1, 2, 3], [4, 5, 6]])
# print(c)

# 还可以接收嵌套元组或元组列表
d = np.array(((1, 2, 3), (4, 5, 6)))
# print(d)

# 可以是由元组或列表组成的列表
e = np.array([(1, 2, 3), [4, 5, 6], (7, 8, 9)])
# print(e)

# ------------------------------------------------------------------------------

# 数据类型
# ------------------------------------------------------------------------------

g = np.array([['a', 'b'], ['c', 'd']])
# print(g)
# print(g.dtype)
# print(g.dtype.name)

# ------------------------------------------------------------------------------


# dtype选项
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------


# 自带的数组创建方法
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
