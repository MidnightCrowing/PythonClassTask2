# map()函数：将函数应用于序列的每个元素
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # 输出：[1，4，9，16，25]

# filter（）函数：过滤序列中的元素，返回满足条件的元素
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2，4]

# sorted（）函数：对序列进行排序，可以指定key为Lambda函数
numbers = [1, 2, 3, 4, 5]
sorted_numbers = sorted(numbers, key=lambda x: -x)
print(sorted_numbers)  # 输出：[5，4，3，2，1]
