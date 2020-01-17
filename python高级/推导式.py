# 列表推导式
# ------------------------------------------------------------------------------


list1 = [i for i in "hello,world"]
# print(list1)

# 还可以加上筛选条件
list2 = [num for num in range(-20, 20) if num % 3 == 0 and num > 0]


# print(list2)


def test(x):
    return x * x


# 可以使用函数
list3 = [test(i) for i in range(0, 10)]
# print(list3)

# 字典推导式
# ------------------------------------------------------------------------------
# 解析列表
li = ['a', 'b', 'c', 'd', 'e']
li_1 = {k: v for k, v in enumerate(li)}
# print(li)

# 解析字典
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {v: k for k, v in dict1.items()}
# print(dict2)


# 集合推导式
# ------------------------------------------------------------------------------
set1 = {x for x in range(10)}
print(set1)
