# `*args`：接受任意数量的位置参数，以元组形式存储。
def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3, 4))


# `**kwargs`：接受任意数量的关键字参数，以字典形式存储。

def greet_all(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


greet_all(name='Charlie', age=25)


# 同时使用 `*args` 和 `**kwargs`：
def process_data(*args, **kwargs):
    # 处理位置参数
    print("位置参数：")
    for arg in args:
        print(arg)

    # 处理关键字参数
    print("关键字参数：")
    for key, value in kwargs.items():
        print(f'{key}: {value}')


# 调用函数，传入任意数量的参数
process_data(1, 2, 3, name="Alice", age=30, location="Wonderland")
