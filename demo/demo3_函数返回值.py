# 1. 使用 return 语句返回一个值
def greet():
    return 'hello'


print(greet())  # 输出：hello


# 2. 使用 return 语句返回多个值，返回值以元组形式传递
def greet_multiple():
    return 'hello', 'world'


# 多个变量接收多个返回值
hello, world = greet_multiple()
print(hello, world)  # 输出：hello world

# 单个变量接收返回的多个值，结果为元组
result = greet_multiple()
print(result)  # 输出：('hello', 'world')


# 使用不匹配数量的变量接收返回值，会报错
# h, e, l = greet_multiple()  # ValueError: not enough values to unpack (expected 3, got 2)


# 3. 使用 return 语句不带任何值，返回 None
def greet_none():
    return


print(greet_none())  # 输出：None


# 4. 函数没有使用 return 语句时，也会返回 None
def fib(n):  # 输出斐波那契数列直到 n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


print(fib(100))  # 输出：None
