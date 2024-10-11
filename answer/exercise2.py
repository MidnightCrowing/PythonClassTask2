# 题目：使用`Lambda`函数计算列表中每个数的平方，并返回结果列表。

numbers = [1, 2, 3, 4, 5]
# 使用map和Lambda计算平方
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # 输出：[1, 4, 9, 16, 25]
