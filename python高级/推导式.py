# 列表推导式
# ------------------------------------------------------------------------------


list1 = [i for i in "hello,world"]
print(list1)

# 还可以加上筛选条件
list2 = [num for num in range(-20, 20) if num % 3 == 0 and num > 0]
print(list2)


def test(x):
    return x * x

# 可以使用函数
list3 = [test(i) for i in range(0, 10)]
print(list3)
