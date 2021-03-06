import numpy as np

# 索引机制
# ------------------------------------------------------------------------------

# 要获取数组的单个元素，指定元素的索引即可
a = np.arange(10, 16)
# print(a)
# print(a[4])
# 还可以使用负数作为索引
# print(a[-1])
# print(a[-6])
# 方括号内传入多个索引值，可以同时选择多个元素
# print(a[[1, 3, 4]])

# 二维数组，它也被称为矩阵
A = np.arange(10, 19).reshape(3, 3)
# print(A)
# 获取第二行第三列的元素
# print(A[1, 2])

# 切片操作
# ------------------------------------------------------------------------------
a = np.arange(10, 16)
# print(a)
# print(a[1:5])
# 间隔为2，表示每隔一个元素抽取一个
# print(a[1:5:2])

# print(a[::2])
# print(a[:5:2])
# print(a[:5:])

A = np.arange(10, 19).reshape((3, 3))
# print(A)

# 只抽取第一行
# print(A[0, :])

# 只抽取第一列
# print(A[:, 0])

# 指定所有的抽取范围
# print(A[0:2, 0:2])

# 如果要抽取的行或列的索引不连续，可以把这几个索引放到数组中
# print(A[[0, 2], 0:2])

# 数组迭代
# ------------------------------------------------------------------------------

for i in a:
    # print(i)
    pass

for row in A:
    # print(row)
    pass

# 遍历矩阵每个元素
for item in A.flat:
    # print(item)
    pass

# 下面这个函数接收三个参数：聚合函数、对哪条轴应用迭代操作、数组
# 如果axis选项的值为0，按列进行迭代操作。为1，按行操作
print(np.apply_along_axis(np.mean, axis=0, arr=A))
print(np.apply_along_axis(np.mean, axis=1, arr=A))


def foo(x):
    return x / 2


print(np.apply_along_axis(foo, axis=1, arr=A))
print(np.apply_along_axis(foo, axis=0, arr=A))
