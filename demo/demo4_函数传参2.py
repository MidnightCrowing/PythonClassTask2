def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)  # 1 个位置参数
parrot(voltage=1000)  # 1 个关键字参数
parrot(voltage=1000000, action='VOOOOOM')  # 2 个关键字参数
parrot(action='VOOOOOM', voltage=1000000)  # 2 个关键字参数
parrot('a million', 'bereft of life', 'jump')  # 3 个位置参数
parrot('a thousand', state='pushing up the daisies')  # 1 个位置参数，1 个关键字参数


# parrot()                     # 缺失必需的参数
# parrot(voltage=5.0, 'dead')  # 关键字参数后存在非关键字参数
# parrot(110, voltage=220)     # 同一个参数重复的值
# parrot(actor='John Cleese')  # 未知的关键字参数


def function(a):
    pass

# function(0, a=0)  # TypeError: function() got multiple values for argument 'a'
