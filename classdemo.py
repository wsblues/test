# classdemo

class person:
    num_person = 0 # class member variable

    def __init__(self):
        # instance member variable
        self.name = "default name"
        person.num_person += 1

    def print(self):
        print("my name is {0}".format(self.name))
        # print('no init')
        # return None     

p0 = person
print(type(p0))
p1 = person()
p1.name = 'wonsuk'
print('instance num : {0}'.format( p1.num_person))
p2 = person()
p2.name = 'yw'
print('instance num : {0}'.format( p1.num_person))

print(type(p1))
p1.print()
p2.print()



