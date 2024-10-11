# 题目：定义一个函数`is_even`，使用`filter()`判断一个数是否为偶数。

# 定义判断偶数的函数
def is_even(n):
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 使用filter()函数过滤出列表中的偶数
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8, 10]
