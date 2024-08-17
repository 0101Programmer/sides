# def __is_valid_sides__(l1, l2, l3, *args):
#     list_ = l1, l2, l3
#     if len(args) == len(list_):
#         if args[0] > 0 and args[0] % 1 == 0 and args[1] > 0 and args[1] % 1 == 0 and args[2] > 0 and args[2] % 1 == 0:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# print(__is_valid_sides__(1, 3, 10, 1, 2, 3))
# print(__is_valid_sides__(1, 3, 10, 1, 2.5, 3))


def __is_valid_sides__2(l1, l2, l3, *args):
    list_ = l1, l2, l3
    if len(args) == len(list_):
        for i in args:
            if i > 0 and i % 1 == 0:
                i += 1
                continue
            else:
                return False
        return True
    else:
        return False


print(__is_valid_sides__2(1, 3, 10, 1, 2, 3))
print(__is_valid_sides__2(1, 3, 10, 1, 2.5, 3))
print('Hello from git')
# some updates
a = 1
b = 2
# проверка изменений
