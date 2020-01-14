import numpy as np

# 连接数组
# ------------------------------------------------------------------------------

A = np.ones((3, 3))
B = np.zeros((3, 3))

# vstack执行垂直入栈操作
# print(np.vstack((A, B)))

# hstack执行水平入栈操作
# print(np.hstack((A, B)))

# 下面这两个函数把一维数组作为列或行压入栈结构，以形成一个新的二维数组
a = np.array([0, 1, 2])
b = np.array([3, 4, 5])
c = np.array([6, 7, 8])

# print(np.column_stack((a, b, c)))
# print(np.row_stack((a, b, c)))

# 数组切分
# ------------------------------------------------------------------------------

A = np.arange(16).reshape((4, 4))
print(A)

# 水平切分数组的意思是把数组按照宽度切分为两部分
[B, C] = np.hsplit(A, 2)
print(B)
print(C)

# 垂直切分指的是把数组按照高度分为两部分
[B, C] = np.vsplit(A, 2)
print(B)
print(C)

# split可以把数组分为几个不对称的部分
# 略

