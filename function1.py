# function1.py
# 220328
def times(a,b):
    return a*b


print(times(2,3))




#immutable

a = 1.2
print(id(a))

a = 2.
print(id(a))


a = (1,2)
print("tuple : ", id(a))
a = (2,3)
print("tuple : ", id(a))
b = a
print("a :", id(a))
print("b :", id(b))


# mutable
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))


def change(x):
    x[0] = "h"


worldlist = ['j', 'a', 'm']
change(worldlist)
print(worldlist)


# deep copy
def change(x):
    x1 = x[:]
    x1[0] = 'h'
    print(x1)


worldlist = ['j', 'a', 'm']
change(worldlist)
print(worldlist)

import copy
demo = {"a":"1", "b":2}
demo2 = copy.deepcopy(demo)
print(id(demo))
print(id(demo2))