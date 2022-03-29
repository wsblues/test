# demoloop

print("--python decision--")

print(bool(0))
print(bool(3))
print(bool(""))
print(bool([]))
lst = [1,2,3,4,5,6]
for i in lst:
    if i > 5:
        break
    print("item:{0}". format(i))
    print("item:{}".format(i))

for i in lst:
    if i%2 == 0:
        continue
    print("item:{0}".format(i))

print("finished")


item = list(range(1,10,2))
print(id(item))
item = list(range(3))
print(id(item))

year = list(range(2000,2020))
print(year)


lst = list(range(1,11))
result = [i**2 for i in lst if i>3]
print(result)

lst = list(range(1,11))

def getBigger(i):
    return i>6

iterl = filter(getBigger, lst)
for item in iterl:
    print("item:{0}".format(item))



iterl = filter(lambda x:x>4, lst)
for item in iterl:
    print("item{0}".format(item))

print([x**2 for x in range(3) if x>1])