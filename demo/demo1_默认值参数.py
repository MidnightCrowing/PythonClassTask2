def greet(name, greeting='Hello', punctuation='!'):
    """返回一个问候语"""
    return f'{greeting}, {name}{punctuation}'


# 只给出必选实参
print('只给出必选实参:')
print(greet('Alice'))  # 输出: Hello, Alice!

# 给出一个可选实参
print('给出一个可选实参:')
print(greet('Bob', 'Hi'))  # 输出: Hi, Bob!

# 给出所有实参
print('给出所有实参:')
print(greet('Charlie', 'Good morning', '.'))  # 输出: Good morning, Charlie.
