# 把句子划分为单词序列
import re
import reprlib

# \w+ 匹配数字和字母下划线的多个字符
re_word = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = re_word.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"


s = Sentence("hello sam haha")
# __repr__方法的作用    __str__方法也可以实现该效果
print(s)

for word in s:
    print(word)

print(list(s))
print(s[0])


# 序列可以迭代的原因:iter函数
class Foo:
    def __iter__(self):
        pass


from collections import abc

f = Foo()
print(isinstance(f, abc.Iterable))
