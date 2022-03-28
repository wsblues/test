# demo.py


from re import A


d = {'apple':'red', "banana":'yellow', 'kiwi':'green'}

print(len(d))
print(d['apple'])
d['grape']='viloet'
print(d)

p = d
print(p)
p['apple']='rose'
print(d)

print(id(d))
print(id(p))
