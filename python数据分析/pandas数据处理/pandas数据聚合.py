import pandas as pd

# groupby
# groupy通常指的是它的内部机制：分组——用函数处理——合并结果 的过程。它的操作由三个阶段组成
# 分组：将数据集分成多个组
# 用函数处理：用函数处理每一组
# 合并：把不同组得到的结果合并起来


# 实例
frame = pd.DataFrame({
    'color': ['white', 'red', 'green', 'red', 'green'],
    'object': ['pen', 'pencil', 'pencil', 'ashtray', 'pen'],
    'price1': [5.56, 4.20, 1.30, 0.56, 2.75],
    'price2': [4.75, 4.12, 1.60, 0.75, 3.15]
})

print(frame)

# 使用color列的组标签，计算price1列的值
group = frame['price1'].groupby(frame['color'])
# print(group)

# 调用group对象的groups属性，可以详细看一下DataFrame各行的分组情况
# print(group.groups)

# 每个组都指定好了它所包含的行。那么，就可以对每组进行操作以获取结果了
# print(group.mean())
# print(group.sum())


# 等级分组
# 上面讲的是用一列元素作为键为数据分组。同理，也可以用很多列，也就是多个键，按照等级关系分组
ggroup = frame['price1'].groupby([frame['color'], frame['object']])
print(ggroup.groups)
print(ggroup.sum())
