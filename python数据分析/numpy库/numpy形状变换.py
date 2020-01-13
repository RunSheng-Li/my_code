import numpy as np

a = np.random.random(12)
print(a)

A = a.reshape(3, 4)
print(A)

# reshape()函数返回一个新数组，因为可用来创建新对象
# 然而，如果想通过改变数组的形状来改变数组对象，需要把表示新形状的元组直接赋值给数组的shape属性
a.shape = (3, 4)
print(a)

# 把二维数组再变回一维数组
# a = a.ravel()
# print(a)

# 甚至直接改变数组shape属性的值也可以
a.shape = (12)
print(a)

# 交换行列位置的矩阵转置
print(A.transpose())
