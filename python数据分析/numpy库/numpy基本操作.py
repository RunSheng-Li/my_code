import numpy as np

# 算术运算符
# ------------------------------------------------------------------------------

a = np.arange(4)
# print(a)

# print(a + 4)
# print(a * 2)

b = np.arange(4, 8)
# print(b)

# print(a + b)
# print(a - b)
# print(a * b)

# 此外，这些运算符还适用于返回值为numpy数组的函数
# print(a * np.sin(b))
# print(a * np.sqrt(b))

# 对于多维数组，这些运算符仍然是元素级
A = np.arange(0, 9).reshape(3, 3)
# print(A)
B = np.ones((3, 3))
# print(B)

# print(A * B)

# 矩阵积
# ------------------------------------------------------------------------------

# print(np.dot(A, B))
# print(A.dot(B))
# print(np.dot(B, A))


# 自增和自减运算符
# ------------------------------------------------------------------------------

# 运算得到的结果不是赋给一个新数组而是赋给参与运算的数组自身
a = np.arange(4)
# print(a)
a += 1
# print(a)
a *= 2
# print(a)

# 通用函数
# ------------------------------------------------------------------------------

a = np.arange(1, 5)
# print(a)
# 计算平方根
# print(np.sqrt(a))

# 取对数
# print(np.log(a))

# 求正弦值
# print(np.sin(a))

# 聚合函数
# ------------------------------------------------------------------------------

a = np.array([3.3, 4.5, 1.2, 5.7, 0.3])
# print(a.sum())
# print(a.min())
# print(a.max())
# print(a.mean())
# 标准差
# print(a.std())
