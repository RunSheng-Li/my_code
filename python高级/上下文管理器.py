# 上下文管理器


# with语句就是简洁版的try/finally语句
# 在日常使用场景中，经常会操作一些资源，比如文件对象、数据库连接、Socket连接等，资源操作完了之后，不管操作的成功与否，最重要的事情就是关闭该资源
f = open('file.txt', 'w')
try:
    f.write('Hello')
finally:
    f.close()

# 但既然close方法是必须的操作，那就没必要显式地调用，所以Python给我们提供了一种更优雅的方式，使用with语句
with open('file1.txt', 'w') as f:
    f.write('Hello')


# 上下文管理器原理
# 把开头的例子用上下文管理器实现一遍
class OpenFile():
    def __init__(self, filename):
        self.file = open(filename, 'w+')

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('file2.txt') as f:
    f.write('Hello')
