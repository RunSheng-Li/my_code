# yield
# ------------------------------------------------------------------------------
def gen():
    n = 0
    while True:
        yield n
        n += 1


g = gen()


# print(g)
# print(next(g))
# print(next(g))

# send
# ------------------------------------------------------------------------------

# 生成器函数可以不断的产出值给调用方，那如果想要调用方传递值给生成器函数呢？

def gen():
    s = yield 'hello'
    print(f'用户传进来的值为{s}')
    yield s


g = gen()
print(next(g))
print(g.send('world'))
