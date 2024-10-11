# noinspection PyDefaultArgument
def append_to_list(value, lst=[]):
    lst.append(value)
    print('lst id:', id(lst))
    return lst


l1 = append_to_list(1)
l2 = append_to_list(2)
l3 = append_to_list(3, [1])
print(l1)
print(l2)
print(l3)
