
b = (i for i in range(5))

print(2 in b)
print(4 in b)
print(3 in b)
print('=======')
########## 输出 ##########

# True
# True
# False

# (i in b) means to do:
# while True:
#     val = next(b)
#     if val == i:
#         yield True


def is_subsequence_(a, b):
    b = iter(b)
    return all(i in b for i in a)

# same as above is_subsequence_
def is_subsequence(a, b):
    gen = (i for i in a)
    print(gen)

    # iterable object a, can be consumed again in the last return line
    for i in gen:
        print(i)

    b = iter(b)
    print(b)

    gen = ((i in b) for i in a)
    print(gen)

    # iterator b, can not be consumed again in the last return line
    # for i in gen:
    #     print(i)

    return all(((i in b) for i in a))


print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))
